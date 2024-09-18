from django import forms
from .models import *

class AddCropForm(forms.ModelForm):
  class Meta:
    model = Crop
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }
class AddUnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }