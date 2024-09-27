from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Crop
from .forms import *
from .forms import SettingsForm
from .models import *

# Create your views here.
# @login_required(login_url="/")
# def settings_view(request):
#   settings = Setting.objects.first()
#   form = SettingsForm(instance=settings)
#   notification = None
#   if request.method == 'POST':
#     form = SettingsForm(data=request.POST,instance=settings)
#     if form.is_valid():
#       form.save()
#       notification = 'success'
#     else:
#       notification = 'failed'


#   return render(request, 'settings.html',{'form':form,'notification':notification})


@login_required(login_url="/")
def crop_view(request,pk=None,notification=None):
  try:
    crop = None
    if pk:
      crop = Crop.objects.get(pk=pk)
    if request.method == 'POST':
      form = CropForm(request.POST,instance=crop)
      if form.is_valid():
        form.save()
        crop = None
        notification = 'success'
      else:
        notification = form.errors.as_text()
        print(form.errors)
  except:
    notification = 'Crop already exists'
  form = CropForm(instance=crop)
  crops = Crop.objects.filter(is_deleted=False)
  return render(request,'master/crops.html',{
    'form':form,
    'crop':crop,
    'crops':crops,
    'notification':notification
  })

@login_required(login_url="/")
def delete_crop(request,pk):
  try:
    crop = Crop.objects.get(id=pk)
    crop.is_deleted = True
    crop.save()
    notification = "deleted"
  except Exception as e:
    notification = str(e)
  print('here')

  return redirect("crop_view",notification=notification)

@login_required(login_url="/")
def unit_view(request,pk=None,notification=None):
  try:
    unit = None
    if pk:
      unit = Unit.objects.get(pk=pk)
    if request.method == 'POST':
      form = UnitForm(request.POST,instance=unit)
      if form.is_valid():
        form.save()
        unit = None
        notification = 'success'
      else:
        notification = 'Unit already exists'
        print(form.errors)
  except:
    notification = 'Unit already exists'
  form = UnitForm(instance=unit)
  units = Unit.objects.all().order_by('-rent_per_month')
  return render(request,'master/units.html',{
    'form':form,
    'unit':unit,
    'units':units,
    'notification':notification
  })
# @login_required(login_url="/")
# def delete_unit(request,pk):
#   try:
#     Unit.objects.get(id=pk).delete()
#     notification = "deleted"
#   except Exception as e:
#     notification = 'error'

#   return redirect("unit_view",notification=notification)


@login_required(login_url="/")
def condition_view(request,pk=None,notification=None):
  try:
    condition = None
    if pk:
      condition = CropCondition.objects.get(pk=pk)
    if request.method == 'POST':
      form = ConditionForm(request.POST,instance=condition)
      if form.is_valid():
        form.save()
        condition = None
        notification = 'success'
      else:
        notification = 'Condition already exists'
        print(form.errors)
  except:
    notification = 'Condition already exists'
  form = ConditionForm(instance=condition)
  conditions = CropCondition.objects.all()
  return render(request,'master/conditions.html',{
    'form':form,
    'condition':condition,
    'conditions':conditions,
    'notification':notification
  })
@login_required(login_url="/")
def delete_condition(request,pk):
  try:
    CropCondition.objects.get(id=pk).delete()
    notification = "deleted"
  except Exception as e:
    notification = "error"

  return redirect("condition_view",notification=notification)

@login_required(login_url="/")
def category_view(request,pk=None,notification=None):
  try:
    category = None
    if pk:
      category = CropCategory.objects.get(pk=pk)
    if request.method == 'POST':
      form = CategoryForm(request.POST,instance=category)
      if form.is_valid():
        form.save()
        category = None
        notification = 'success'
      else:
        notification = 'Category already exists'
        print(form.errors)
  except:
    notification = 'Category already exists'
  form = CategoryForm(instance=category)
  categories = CropCategory.objects.all()
  return render(request,'master/categories.html',{
    'form':form,
    'category':category,
    'categories':categories,
    'notification':notification
  })
@login_required(login_url="/")
def delete_category(request,pk):
  try:
    CropCategory.objects.get(id=pk).delete()
    notification = "deleted"
  except Exception as e:
    notification = "error"

  return redirect("category_view",notification=notification)

@login_required(login_url="/")
def insurance_view(request,pk=None,notification=None):
  try:
    insurance = None
    if pk:
      insurance = Insurance.objects.get(pk=pk)
    if request.method == 'POST':
      form = InsuranceForm(request.POST,instance=insurance)
      if form.is_valid():
        form.save()
        insurance = None
        notification = 'success'
      else:
        notification = 'Insurance already exists'
        print(form.errors)
  except:
    notification = 'Insurance already exists'
  form = InsuranceForm(instance=insurance)
  insurances = Insurance.objects.filter(is_deleted=False)
  return render(request,'master/insurances.html',{
    'form':form,
    'insurance':insurance,
    'insurances':insurances,
    'notification':notification
  })
@login_required(login_url="/")
def delete_insurance(request,pk):
  try:
    insurance = Insurance.objects.get(id=pk)
    insurance.is_deleted = True
    insurance.save()
    notification = "deleted"
  except Exception as e:
    notification = 'error'
  return redirect("insurance_view",notification=notification)

@login_required(login_url="/")
def section_view(request,pk=None,notification=None):
  try:
    section = None
    if pk:
      section = Section.objects.get(pk=pk)
    if request.method == 'POST':
      form = SectionForm(request.POST,instance=section)
      if form.is_valid():
        form.save()
        section = None
        notification = 'success'
      else:
        notification = 'Section already exists'
        print(form.errors)
  except:
    notification = 'Section already exists'
  form = SectionForm(instance=section)
  sections = Section.objects.all()
  return render(request,'master/sections.html',{
    'form':form,
    'section':section,
    'sections':sections,
    'notification':notification
  })
@login_required(login_url="/")
def delete_section(request,pk):
  try:
    Section.objects.get(id=pk).delete()
    notification = "deleted"
  except Exception as e:
    notification = "error"

  return redirect("section_view",notification=notification)

