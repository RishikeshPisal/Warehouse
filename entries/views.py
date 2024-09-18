from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Entry
from .forms import AddEntryForm
# Create your views here.

@login_required(login_url="/")
def all_entries_view(request):
  entries = Entry.objects.all().order_by('-arrival_time','-departure_time')
  return render(request, 'entries/all_entries.html',{'entries':entries})  

@login_required(login_url="/")
def add_entry_view(request,notification=None):
  form = AddEntryForm()
  if request.method == 'POST':
    form = AddEntryForm(request.POST)
    if form.is_valid():
      form.save()
      notification = 'success'
    else:
      notification = 'failed'
    return redirect('add_entry_view',notification=notification)
  return render(request, 'entries/add_entry.html',{'form':form,'notification':notification})



@login_required(login_url="/")
def update_entry_view(request,pk=None):
  entry = Entry.objects.get(id=pk)
  notification = None
  if request.method == 'POST':
    form = AddEntryForm(request.POST,instance=entry)
    if form.is_valid():
      entry = form.save()
      notification = 'success'
    else:
      print(form.errors)
      notification = 'failed'

  form = AddEntryForm(instance=entry)
  return render(request,'entrys/update_entry.html',{'form':form,'notification':notification,'entry':entry})

# @login_required(login_url='/')
