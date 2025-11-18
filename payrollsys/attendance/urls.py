from django.urls import path
from .views import AttendanceListView, AttendanceCreateView, AttendanceUpdateView, AttendanceDeleteView

app_name = 'attendance'

urlpatterns = [
    path('', AttendanceListView.as_view(), name='list'),
    path('add/', AttendanceCreateView.as_view(), name='add'),
    path('<int:pk>/edit/', AttendanceUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete/', AttendanceDeleteView.as_view(), name='delete'),
]
