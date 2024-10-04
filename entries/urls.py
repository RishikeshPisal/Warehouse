from django.urls import path,re_path
from .views import *


urlpatterns = [
  # re_path(r'^settings(?:/(?P<notification>[\w-]+))?/$', settings_view, name="settings_view"),
  re_path(r'^inward(?:/(?P<notification>[\w-]+))?/$', inward_view, name="inward_view"),
  re_path(r'^view(?:/(?P<pk>\d+))?/$', disabled_inward_view, name="disabled_inward_view"),
  re_path(r'^pay(?:/(?P<notification>[\w-]+))?/$', pay_view, name="pay_view"),
  re_path(r'^pay_rent(?:/(?P<pk>\d+))?/$', pay_rent, name="pay_rent"),
  re_path(r'^pay_interest(?:/(?P<pk>\d+))?/$', pay_interest, name="pay_interest"),
  re_path(r'^payment_summary(?:/(?P<pk>\d+))?/$', payment_summary, name="payment_summary"),
  re_path(r'^outward(?:/(?P<notification>[\w-]+))?/$', outward_view, name="outward_view"),
  re_path(r'^outward/entry/(?P<pk>\d+)/$', outward_entry_view, name="outward_entry_view"),

  # path('create/',inward_view,name="inward_view"),
  path('all/',all_entries_view,name="all_entries_view")
]
