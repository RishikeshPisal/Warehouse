
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

########################### Models #################################
from entries.models import Entry
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
    print('here')
    return render(request,'dashboard.html',{'entries':entries})



