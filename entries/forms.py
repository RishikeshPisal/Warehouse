from .models import *
from customers.models import Customer
from configurations.models import *
from django import forms


class AddEntryForm(forms.ModelForm):
  class Meta:
    model = Entry
    fields = ['customer','crop','sacks','weight',
              'unit','crop_category','crop_condition',
              'price_per_unit','section','insurance_till',
              'policy_no','other_details',
              'vehicle_no','driver_name',]
    widgets = {
        'customer': forms.Select(attrs={'class': 'form-control form-control-lg','id':'customer'}),
        'sacks': forms.NumberInput(attrs={'class': 'form-control','id':'sacks'}),
        'weight': forms.NumberInput(attrs={'class': 'form-control','id':'weight'}),
        'price_per_unit': forms.NumberInput(attrs={'class': 'form-control','id':'price_per_unit'}),
        'insurance_till': forms.DateInput(attrs={'type':'date','class': 'form-control','id':'insurance_till'}),
        'vehicle_no': forms.TextInput(attrs={'class': 'form-control','id':'vehicle_no'}),
        'driver_name': forms.TextInput(attrs={'class': 'form-control','id':'driver_name'}),
        'policy_no': forms.TextInput(attrs={'class': 'form-control','id':'policy_no'}),
        'other_details': forms.TextInput(attrs={'class': 'form-control','id':'other_details'}),
    }
  unit = forms.ModelChoiceField(
    label='Unit',
    queryset=Unit.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'unit'})
  )
  crop = forms.ModelChoiceField(
    label='Crop',
    queryset=Crop.objects.filter(is_deleted=False),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'crop'})
  )
  crop_category = forms.ModelChoiceField(
    label='Crop Category',
    queryset=CropCategory.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'crop_category'})
  )
  crop_condition = forms.ModelChoiceField(
    label='Crop Condition',
    queryset=CropCondition.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'crop_condition'})
  )
  insurance = forms.ModelChoiceField(
    label='Insurance',
    queryset=Insurance.objects.filter(is_deleted=False),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'insurance'})
  )
  section = forms.ModelChoiceField(
    label='Section',
    queryset=Section.objects.all(),
    widget=forms.Select(attrs={'class': 'form-control py-3','id':'section'})
  )



# class RentHistoryForm(forms.ModelForm):
#   class Meta:
#     model = RentHistory
#     fields = ['amount']
#     widgets = {
#         'amount': forms.NumberInput(attrs={'class': 'form-control','id':'amount'}),
#     }