from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import AddEntryForm
# Create your views here.

@login_required(login_url="/")
def all_entries_view(request):
  entries = Entry.objects.all().order_by('-arrival_time','-departure_time')
  return render(request, 'entries/all_entries.html',{'entries':entries})  

@login_required(login_url="/")
def add_entry_view(request,notification=None):
  form = AddEntryForm()
  loan_amount_percentage = None
  customers = Customer.objects.all()
  try:
    loan_amount_percentage = Setting.objects.first().load_amount_percentage
    if request.method == 'POST':
      form = AddEntryForm(request.POST)
      if form.is_valid():
        form.save()
        notification = 'success'
      else:
        notification = form.errors.as_text()
      return redirect('add_entry_view',notification=notification)
  except Exception as e:
    print('problem')
    notification = str(e)
  return render(request, 'entries/add_entry.html',{
    'form':form,
    'notification':notification,
    'customers':customers,
    'loan_amount_percentage':loan_amount_percentage,
  })



@login_required(login_url="/")
def update_entry_view(request,pk=None):
  try:
    entry = Entry.objects.get(id=pk)
    notification = None
    if request.method == 'POST':
      form = AddEntryForm(request.POST,instance=entry)
      if form.is_valid():
        entry = form.save()
        notification = 'success'
      else:
        print(form.errors.as_text())
        notification = form.errors.as_text()
        # notification = 'failed'
  except Exception as e:
    notification = str(e)
  form = AddEntryForm(instance=entry)
  return render(request,'entrys/update_entry.html',{'form':form,'notification':notification,'entry':entry})

@login_required(login_url='/')
def pay_rent(request,pk):
  try:
    amount = int(request.POST.get('amount'))
    entry = Entry.objects.get(id=pk)
    entry.rent_paid += amount
    entry.save()
    notification = "Rent Updated"
    RentHistory.objects.create(entry=entry,amount=amount)
  except Exception as e:
    notification = str(e)
  return redirect('all_entries_view',notification=notification)

