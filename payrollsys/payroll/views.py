from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import PayrollRecord
from .forms import PayrollRecordForm

class PayrollListView(LoginRequiredMixin, ListView):
    model = PayrollRecord
    template_name = 'payroll/payroll_list.html'
    context_object_name = 'records'

class PayrollDetailView(LoginRequiredMixin, DetailView):
    model = PayrollRecord
    template_name = 'payroll/payroll_detail.html'
    context_object_name = 'record'

class PayrollCreateView(LoginRequiredMixin, CreateView):
    model = PayrollRecord
    form_class = PayrollRecordForm
    template_name = 'payroll/payroll_form.html'
    success_url = reverse_lazy('payroll:list')
