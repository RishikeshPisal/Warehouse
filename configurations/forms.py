from .models import Setting
from django import forms


class SettingsForm(forms.ModelForm):
  class Meta:
    model = Setting
    fields = ['rent_per_day','loan_interest']
    widgets = {
        'rent_per_day': forms.NumberInput(attrs={'class': 'form-control','id':'name'}),
        'loan_interest': forms.NumberInput(attrs={'class': 'form-control','id':'address'}),
    }