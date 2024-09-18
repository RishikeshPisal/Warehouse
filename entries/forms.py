from .models import Entry
from customers.models import Customer
from crops.models import Crop
from django import forms


class AddEntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['customer','crop','sacks','weight','unit','price_per_unit']
    widgets = {
        'customer': forms.Select(attrs={'class': 'form-control form-control-lg','id':'address'}),
        'crop': forms.Select(attrs={'class': 'form-control form-control-lg','id':'address'}),
        'unit': forms.Select(attrs={'class': 'form-control form-control-lg','id':'address'}),
        'sacks': forms.NumberInput(attrs={'class': 'form-control','id':'address'}),
        'weight': forms.NumberInput(attrs={'class': 'form-control','id':'address'}),
        'price_per_unit': forms.NumberInput(attrs={'class': 'form-control','id':'address'}),
    }
  # customer = forms.ModelChoiceField(
  #   label='Customer',
  #   queryset=Customer.objects.all(),
  #   widget=forms.Select(attrs={'class': 'form-control py-3','id':'customer'})
  #   ),
  # crop = forms.ModelChoiceField(
  #   label='Crop',
  #   queryset=Customer.objects.all(),
  #   widget=forms.Select(attrs={'class': 'form-control py-3','id':'crop'})
  #   ),