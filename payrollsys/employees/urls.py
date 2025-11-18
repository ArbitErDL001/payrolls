from django.urls import path
from . import views

app_name = 'employees'

urlpatterns = [
    path('', views.EmployeeListView.as_view(), name='list'),
    path('add/', views.EmployeeCreateView.as_view(), name='add'),
    path('<str:employee_id>/', views.EmployeeDetailView.as_view(), name='detail'),
    path('<str:employee_id>/edit/', views.EmployeeUpdateView.as_view(), name='edit'),
    path('<str:employee_id>/delete/', views.EmployeeDeleteView.as_view(), name='delete'),
]