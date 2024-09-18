from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Customer
from .forms import AddCustomerForm
# Create your views here.


@login_required(login_url="/")
def add_customer_view(request):
  notification = None
  if request.method == 'POST':
    form = AddCustomerForm(request.POST)
    if form.is_valid():
      customer = form.save()
      notification = 'success'
    else:
      print(form.errors)
      notification = 'failed' 

  form = AddCustomerForm()
  return render(request,'customers/add_customer.html',{'form':form,'notification':notification})

@login_required(login_url="/")
def update_customer_view(request,pk=None):
  customer = Customer.objects.get(id=pk)
  notification = None
  if request.method == 'POST':
    form = AddCustomerForm(request.POST,instance=customer)
    if form.is_valid():
      customer = form.save()
      notification = 'success'
    else:
      print(form.errors)
      notification = 'failed'

  form = AddCustomerForm(instance=customer)
  return render(request,'customers/update_customer.html',{'form':form,'notification':notification,'customer':customer})

@login_required(login_url="/")
def all_customers_view(request):
  customers = Customer.objects.all()
  return render(request, 'customers/all_customers.html',{'customers':customers})
