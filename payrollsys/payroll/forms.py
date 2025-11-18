from django import forms
from .models import PayrollRecord

class PayrollRecordForm(forms.ModelForm):
    class Meta:
        model = PayrollRecord
        fields = ['employee', 'cutoff_start', 'cutoff_end', 'pay_structure']
