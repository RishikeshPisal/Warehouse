from django.urls import path
from .views import *


urlpatterns = [
  path('',login_view,name='login_view'),
  path('dashboard',home,name='home'),
]