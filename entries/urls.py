from django.urls import path,re_path
from .views import *


urlpatterns = [
  # re_path(r'^settings(?:/(?P<notification>[\w-]+))?/$', settings_view, name="settings_view"),
  re_path(r'^create(?:/(?P<notification>[\w-]+))?/$', inward_view, name="inward_view"),
  re_path(r'^view(?:/(?P<pk>\d+))?/$', disabled_inward_view, name="disabled_inward_view"),
  re_path(r'^pay(?:/(?P<notification>[\w-]+))?/$', pay_view, name="pay_view"),
  re_path(r'^pay_rent(?:/(?P<pk>\d+))?/$', pay_rent, name="pay_rent"),

  # path('create/',inward_view,name="inward_view"),
  path('all/',all_entries_view,name="all_entries_view")
]
