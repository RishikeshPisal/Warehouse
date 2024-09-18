from .models import Customer
from django import forms


class AddCustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name','address','city','pin_code','state','contact_number','email']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),
        'address': forms.TextInput(attrs={'class': 'form-control','id':'address'}),
        'city': forms.TextInput(attrs={'class': 'form-control','id':'city'}),
        'pin_code': forms.TextInput(attrs={'class': 'form-control','id':'pin_code'}),
        'state': forms.TextInput(attrs={'class': 'form-control','id':'state'}),
        'contact_number': forms.TextInput(attrs={'class': 'form-control','id':'contact_number'}),
        'email': forms.EmailInput(attrs={'class': 'form-control','id':'email'}),
    }