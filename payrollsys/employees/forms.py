from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = [
            'first_name', 'last_name', 'middle_name',
            'position', 'department', 'employment_type',
            'email', 'phone', 'national_id', 'date_hired', 'is_active'
        ]

    def clean(self):
        cleaned = super().clean()
        email = cleaned.get('email')
        national_id = cleaned.get('national_id', '').strip()
        phone = cleaned.get('phone', '').strip()

        if not email:
            self.add_error('email', 'Email is required.')
        # Optional: require either national_id or phone for contact/ID
        if not national_id and not phone:
            raise forms.ValidationError('Provide either a National ID (e.g., TIN/SSS) or a phone number.')

        return cleaned