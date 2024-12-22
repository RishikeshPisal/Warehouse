
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from entries.models import Entry
from customers.models import Customer
from configurations.models import Crop


####################################################################

def login_view(request):
    notification = True
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            notification = False
    return render(request, 'login.html',{'notification':notification})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def home(request):
    entries = Entry.objects.all().order_by('-arrival_date','-departure_date')
    total_sacks = 0
    total_weight = 0
    total_pending_principle = 0
    total_pending_interest = 0
    total_pending_rent = 0
    for entry in entries:
        total_sacks += entry.sacks
        total_weight += entry.weight
        total_pending_principle += entry.total_principle
        total_pending_interest  += entry.total_pending_interest()
        total_pending_rent  += entry.total_pending_rent()
    total_customers = Customer.objects.all().count()
    total_crops = Crop.objects.all().count()
    
    return render(request,'dashboard.html',{
        'entries':entries,
        'total_sacks':total_sacks,
        'total_weight':total_weight,
        'total_pending_interest':total_pending_interest,
        'entries':entries,
    })



