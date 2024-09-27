from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, F
from .models import *
from .forms import AddEntryForm
# Create your views here.

@login_required(login_url="/")
def all_entries_view(request):
  entries = Entry.objects.all().order_by('-arrival_time','-departure_time')
  customers = Customer.objects.all()
  crops = Crop.objects.all()
  total_sacks = Entry.objects.aggregate(Sum('sacks'))['sacks__sum']
  loan_amount_percentage = Setting.objects.first().loan_amount_percentage
  total_due_rent = sum((entry.get_due_rent() for entry in entries))
  total_due_interest = sum((entry.get_due_interest() for entry in entries))
  entries = entries.filter(closed=False)

  total_loan_given = Entry.objects.aggregate(
    total_loan=Sum(F('weight')*F('price_per_unit'))
  )['total_loan']
  # print(total_loan_given)
  return render(request, 'entries/all_entries.html',{
    'entries':entries,
    'customers':customers,
    'crops':crops,
    'total_sacks':total_sacks if total_sacks else 0, 
    'total_due_rent':total_due_rent,
    'total_due_interest':total_due_interest,
    'total_loan_given':(total_loan_given*loan_amount_percentage)//100 if total_loan_given else 0,
  })  

@login_required(login_url="/")
def inward_view(request,notification=None):
  form = AddEntryForm()
  loan_amount_percentage = None
  customers = Customer.objects.all()
  try:
    loan_amount_percentage = Setting.objects.first().loan_amount_percentage
    if request.method == 'POST':
      form = AddEntryForm(request.POST)
      if form.is_valid():
        form.save()
        notification = 'success'
      else:
        notification = form.errors.as_text()
      return redirect('inward_view',notification=notification)
  except Exception as e:
    print('problem')
    notification = str(e)
  return render(request, 'entries/inward.html',{
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
  return render(request,'entries/update_entry.html',{'form':form,'notification':notification,'entry':entry})

@login_required(login_url="/")
def disabled_inward_view(request,pk=None):
  try:
    entry = Entry.objects.get(id=pk)
    loan_amount_percentage = Setting.objects.first().loan_amount_percentage
    notification = None
    form = AddEntryForm(instance=entry)
    total_price = entry.weight*entry.price_per_unit
    loan_amount = (total_price*loan_amount_percentage)//100
    

  except Exception as e:
    notification = str(e)
  return render(request,'entries/disabled_inward.html',{
    'form':form,
    'notification':notification,
    'entry':entry,
    'loan_amount_percentage':loan_amount_percentage,
    'total_price':total_price,
    'loan_amount':loan_amount,
    })

@login_required(login_url='/')
def pay_view(request):
  entries = Entry.objects.all().order_by('-arrival_time','-departure_time')
  customers = Customer.objects.all()
  crops = Crop.objects.all()
  # total_sacks = Entry.objects.aggregate(Sum('sacks'))['sacks__sum']
  # loan_amount_percentage = Setting.objects.first().loan_amount_percentage
  # total_due_rent = sum((entry.get_due_rent() for entry in entries))
  # total_due_interest = sum((entry.get_due_interest() for entry in entries))
  entries = entries.filter(closed=False)

  # total_loan_given = Entry.objects.aggregate(
  #   total_loan=Sum(F('weight')*F('price_per_unit'))
  # )['total_loan']

  return render(request, 'entries/pay.html',{
    'entries':entries,
    'customers':customers,
    'crops':crops,
    # 'total_sacks':total_sacks if total_sacks else 0, 
    # 'total_due_rent':total_due_rent,
    # 'total_due_interest':total_due_interest,
    # 'total_loan_given':(total_loan_given*loan_amount_percentage)//100 if total_loan_given else 0,
  })      


@login_required(login_url='/')
def pay_rent(request,pk):
  try:
    amount = int(request.POST.get('amount'))
    entry = Entry.objects.get(id=pk)
    entry.rent_paid += amount
    # entry.save()
    notification = "Rent Updated"
    print('works',entry,amount)
    # RentHistory.objects.create(entry=entry,amount=amount)
  except Exception as e:
    notification = str(e)
    print(notification)
  return redirect('all_entries_view',notification=notification)

@login_required(login_url='/')
def outward_view(request,pk):
  try:
    entry = Entry.objects.get(pk=pk)
    if request.method == 'POST':
      amount = int(request.POST.get('amount'))
      sacks = int(request.POST.get('sacks'))
      rent_history = RentHistory.objects.create(entry=entry,amount=amount)
      Outward.objects.create(rent_history=rent_history,sacks=sacks)
      notification = 'success'
      return render('all_entries_view',notification=notification)
    else:
      notification = None
  except Exception as e:
    notification = str(e)
  return render(request,'entries/outward.html',{
    'notification':notification
  })
