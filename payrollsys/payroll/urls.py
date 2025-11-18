from django.urls import path
from .views import PayrollListView, PayrollDetailView, PayrollCreateView

app_name = 'payroll'

urlpatterns = [
    path('', PayrollListView.as_view(), name='list'),
    path('add/', PayrollCreateView.as_view(), name='add'),
    path('<int:pk>/', PayrollDetailView.as_view(), name='detail'),
]
