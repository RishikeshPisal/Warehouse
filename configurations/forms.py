from .models import Setting
from django import forms
from django import forms
from .models import *


class SettingsForm(forms.ModelForm):
  class Meta:
    model = Setting
    fields = ['loan_interest']
    widgets = {
        'loan_interest': forms.NumberInput(attrs={'class': 'form-control','id':'address'}),
    }

class CropForm(forms.ModelForm):
  class Meta:
    model = Crop
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }

  def clean_name(self):
    name = self.cleaned_data.get('name').title()
    filtered_set = Crop.objects.filter(name=name)
    if filtered_set.exists():
      crop = filtered_set[0]
      if crop.is_deleted:
        crop.is_deleted = False
        crop.save()
      else:
        raise Exception("Crop already exists ")
    return name.title()


class UnitForm(forms.ModelForm):
  class Meta:
    model = Unit
    fields = ['name','rent_per_month']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),
        'rent_per_month': forms.NumberInput(attrs={'class': 'form-control','id':'relative_value'}),

    }
class ConditionForm(forms.ModelForm):
  class Meta:
    model = CropCondition
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }
class CategoryForm(forms.ModelForm):
  class Meta:
    model = CropCategory
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }
class InsuranceForm(forms.ModelForm):
  class Meta:
    model = Insurance
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),
    }
  def clean_name(self):
    name = self.cleaned_data.get('name').title()
    filtered_set = Insurance.objects.filter(name=name)
    if filtered_set.exists():
      insurance = filtered_set[0]
      if insurance.is_deleted:
        insurance.is_deleted = False
        insurance.save()
      else:
        raise Exception("Insurance already exists ")
    return name.title()


class SectionForm(forms.ModelForm):
  class Meta:
    model = Section
    fields = ['name']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control','id':'name'}),

    }