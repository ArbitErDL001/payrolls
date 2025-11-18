from django.db import models
from django.utils import timezone

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f'{self.code} - {self.name}'


class Position(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    EMPLOYMENT_TYPES = [
        ('REG', 'Regular'),
        ('CON', 'Contractual'),
        ('PT', 'Part-time'),
        ('PRB', 'Probationary'),
    ]

    employee_id = models.CharField(max_length=20, unique=True, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    position = models.ForeignKey(Position, on_delete=models.PROTECT)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    employment_type = models.CharField(max_length=4, choices=EMPLOYMENT_TYPES)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)
    national_id = models.CharField(max_length=30, blank=True)  # e.g., TIN or SSS number
    date_hired = models.DateField(default=timezone.now)
    is_active = models.BooleanField(default=True)  # useful for soft-offboarding

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['department']),
        ]
        constraints = [
            models.UniqueConstraint(
                fields=['national_id'],
                name='unique_national_id',
                condition=~models.Q(national_id='')
            ),
        ]

    def save(self, *args, **kwargs):
        if not self.employee_id:
            # Generate EMP-YYYY-XXXX sequence per year
            year = timezone.now().year
            prefix = f'EMP-{year}-'
            last = Employee.objects.filter(employee_id__startswith=prefix).order_by('employee_id').last()
            if last:
                try:
                    seq = int(last.employee_id.split('-')[-1]) + 1
                except ValueError:
                    seq = 1
            else:
                seq = 1
            self.employee_id = f'{prefix}{seq:04d}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.employee_id} - {self.last_name}, {self.first_name}'