from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Crop
from .forms import *
# Create your views here.




@login_required(login_url="/")
def all_crops_view(request,pk=None,notification=None):
  crops = Crop.objects.filter(is_deleted=False)

  return render(request,'crops/all_crops.html',{'crops':crops})


@login_required(login_url="/")
def add_crop_view(request,pk=None,notification=None):
  try:
    if request.method == 'POST':
      form = AddCropForm(request.POST)
      if form.is_valid():
        form.save()
        notification = 'success'
      else:
        print(form.errors)
  except Exception as e:
    notification = str(e)

  form = AddCropForm()
  return render(request,'crops/add_crop.html',{'form':form,'notification':notification})

@login_required(login_url="/")
def update_crop_view(request,pk=None):
  try:
    crop = Crop.objects.get(id=pk)
    notification = None
    if request.method == 'POST':
      form = AddCropForm(request.POST,instance=crop)
      if form.is_valid():
        form.save()
        notification = 'success'
      else:
        notification = 'failed'
        print(form.errors)
  except Exception as e:
    notification = str(e)

  form = AddCropForm(instance=crop)
  return render(request,'crops/update_crop.html',{'form':form,'crop':crop,'notification':notification})

@login_required(login_url="/")
def delete_crop(request,pk=None):
  try:
    crop = Crop.objects.get(id=pk)
    crop.is_deleted = True
  except Exception as e:
    notification = str(e)

    return redirect('all_crops_view',notification=notification)


@login_required(login_url="/")
def all_crops_view(request,pk=None,notification=None):
  crops = Crop.objects.filter(is_deleted=False)

  return render(request,'crops/all_crops.html',{'crops':crops})


@login_required(login_url="/")
def add_unit_view(request,pk=None,notification=None):
  try:  
    if request.method == 'POST':
      form = AddUnitForm(request.POST)
      if form.is_valid():
        form.save()
        notification = 'success'
      else:
        notification = 'Unit already exists'
        print(form.errors)
  except:
    notification = 'Unit already exists'
  form = AddUnitForm()
  units = Unit.objects.all()
  return render(request,'crops/add_unit.html',{
    'form':form,
    'units':units,
    'notification':notification
  })



