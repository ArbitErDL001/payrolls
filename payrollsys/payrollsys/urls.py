from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth.views import LoginView
from employees.views import HomeView

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='employees:list', permanent=False)),
    path('admin/', admin.site.urls),
    path('employees/', include('employees.urls')),
    path('attendance/', include('attendance.urls')),
    path('payroll/', include('payroll.urls')),
    path('my-login/', LoginView.as_view(), name='login'),
]
