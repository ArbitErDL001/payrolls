from django.contrib import admin
from .models import Department, Position, Employee

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')
    search_fields = ('code', 'name')

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'last_name', 'first_name', 'department', 'position', 'employment_type', 'email', 'is_active')
    list_filter = ('department', 'position', 'employment_type', 'is_active')
    search_fields = ('employee_id', 'last_name', 'first_name', 'email', 'national_id')