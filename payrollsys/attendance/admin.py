from django.contrib import admin
from .models import AttendanceLog

@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'time_in', 'time_out', 'is_absent', 'overtime_hours', 'total_hours')
    list_filter = ('date', 'is_absent')
    search_fields = ('employee__employee_id', 'employee__last_name')