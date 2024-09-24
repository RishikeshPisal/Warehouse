from .models import Customer
from django import forms


class AddCustomerForm(forms.ModelForm):
  class Meta:
    model = Customer
    fields = ['name','taluka','zila','contact_number','email']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),
        'taluka': forms.TextInput(attrs={'class': 'form-control','id':'taluka'}),
        'zila': forms.TextInput(attrs={'class': 'form-control','id':'zila'}),
        'contact_number': forms.TextInput(attrs={'class': 'form-control','id':'contact_number'}),
        'email': forms.EmailInput(attrs={'class': 'form-control','id':'email'}),
    } 