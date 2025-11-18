from django.contrib import admin
from .models import PayrollRecord

@admin.register(PayrollRecord)
class PayrollRecordAdmin(admin.ModelAdmin):
    list_display = ('employee', 'cutoff_start', 'cutoff_end', 'gross_pay', 'net_pay')
    list_filter = ('pay_structure', 'cutoff_end')
    search_fields = ('employee__employee_id', 'employee__last_name')
