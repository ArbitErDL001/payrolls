from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import AttendanceLog
from .forms import AttendanceLogForm

class AttendanceListView(LoginRequiredMixin, ListView):
    model = AttendanceLog
    template_name = 'attendance/attendance_list.html'
    context_object_name = 'logs'
    paginate_by = 30

    def get_queryset(self):
        qs = AttendanceLog.objects.select_related('employee')
        emp = self.request.GET.get('employee')
        if emp:
            qs = qs.filter(employee__employee_id__icontains=emp)
        return qs

class AttendanceCreateView(LoginRequiredMixin, CreateView):
    model = AttendanceLog
    form_class = AttendanceLogForm
    template_name = 'attendance/attendance_form.html'
    success_url = reverse_lazy('attendance:list')

class AttendanceUpdateView(LoginRequiredMixin, UpdateView):
    model = AttendanceLog
    form_class = AttendanceLogForm
    template_name = 'attendance/attendance_form.html'
    success_url = reverse_lazy('attendance:list')

class AttendanceDeleteView(LoginRequiredMixin, DeleteView):
    model = AttendanceLog
    template_name = 'attendance/attendance_confirm_delete.html'
    success_url = reverse_lazy('attendance:list')
