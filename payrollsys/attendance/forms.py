from django import forms
from .models import AttendanceLog

class AttendanceLogForm(forms.ModelForm):
    class Meta:
        model = AttendanceLog
        fields = ['employee', 'date', 'time_in', 'time_out', 'is_absent', 'overtime_hours']

    def clean(self):
        cleaned = super().clean()
        time_in = cleaned.get('time_in')
        time_out = cleaned.get('time_out')
        absent = cleaned.get('is_absent')

        if not absent and (not time_in or not time_out):
            raise forms.ValidationError("Provide time-in and time-out unless marked absent.")
        if time_in and time_out and time_out <= time_in:
            raise forms.ValidationError("Time-out must be later than time-in.")
        return cleaned