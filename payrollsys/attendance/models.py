from django.db import models
from django.utils import timezone
from employees.models import Employee

class AttendanceLog(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendance_logs')
    date = models.DateField(default=timezone.now)
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)
    is_absent = models.BooleanField(default=False)
    overtime_hours = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        unique_together = ('employee', 'date')
        ordering = ['-date']

    def total_hours(self):
        if self.is_absent or not self.time_in or not self.time_out:
            return 0
        delta = timezone.datetime.combine(self.date, self.time_out) - timezone.datetime.combine(self.date, self.time_in)
        return round(delta.total_seconds() / 3600, 2)

    def __str__(self):
        return f'{self.employee.employee_id} - {self.date}'
