from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import Employee

class MyLoginView(LoginView):
    template_name = 'registration/login.html'

class HomeView(TemplateView):
    template_name = 'home.html'


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'employees'
    paginate_by = 20


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employees/employee_detail.html'
    context_object_name = 'employee'
    slug_field = 'employee_id'
    slug_url_kwarg = 'employee_id'


class EmployeeCreateView(CreateView):
    model = Employee
    fields = [
        'first_name', 'last_name', 'middle_name', 'position', 'department',
        'employment_type', 'email', 'phone', 'national_id', 'date_hired', 'is_active'
    ]
    template_name = 'employees/employee_form.html'
    success_url = reverse_lazy('employees:list')


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = [
        'first_name', 'last_name', 'middle_name', 'position', 'department',
        'employment_type', 'email', 'phone', 'national_id', 'date_hired', 'is_active'
    ]
    template_name = 'employees/employee_form.html'
    slug_field = 'employee_id'
    slug_url_kwarg = 'employee_id'
    success_url = reverse_lazy('employees:list')


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employees/employee_confirm_delete.html'
    slug_field = 'employee_id'
    slug_url_kwarg = 'employee_id'
    success_url = reverse_lazy('employees:list')
