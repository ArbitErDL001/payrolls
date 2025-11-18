from django.db import models
from django.utils import timezone
from employees.models import Employee
from attendance.models import AttendanceLog

class PayrollRecord(models.Model):
    PAY_STRUCTURES = [
        ('MONTHLY', 'Monthly'),
        ('WEEKLY', 'Weekly'),
        ('DAILY', 'Daily'),
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_records')
    cutoff_start = models.DateField()
    cutoff_end = models.DateField()
    pay_structure = models.CharField(max_length=10, choices=PAY_STRUCTURES, default='MONTHLY')

    gross_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_pay = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def compute_gross(self):
        logs = AttendanceLog.objects.filter(
            employee=self.employee,
            date__range=(self.cutoff_start, self.cutoff_end)
        )
        total_hours = sum([log.total_hours() + float(log.overtime_hours) for log in logs])
        hourly_rate = getattr(self.employee.position, 'hourly_rate', 100)  # placeholder
        self.gross_pay = round(total_hours * hourly_rate, 2)
        return self.gross_pay

    def compute_deductions(self):
        # Simple rule: 15% of gross pay
        self.deductions = round(self.gross_pay * 0.15, 2)
        return self.deductions

    def compute_net(self):
        self.net_pay = self.gross_pay - self.deductions
        return self.net_pay

    def save(self, *args, **kwargs):
        self.compute_gross()
        self.compute_deductions()
        self.compute_net()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee.employee_id} | {self.cutoff_start} - {self.cutoff_end}'
