from django.urls import path,re_path
from .views import *


urlpatterns = [
  # re_path(r'^settings(?:/(?P<notification>[\w-]+))?/$', settings_view, name="settings_view"),
  path('',settings_view,name="settings_view")

]
