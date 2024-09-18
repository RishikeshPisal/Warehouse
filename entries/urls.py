from django.urls import path,re_path
from .views import *


urlpatterns = [
  # re_path(r'^settings(?:/(?P<notification>[\w-]+))?/$', settings_view, name="settings_view"),
  re_path(r'^create(?:/(?P<notification>[\w-]+))?/$', add_entry_view, name="add_entry_view"),

  # path('create/',add_entry_view,name="add_entry_view"),
  path('all/',all_entries_view,name="all_entries_view")
]
