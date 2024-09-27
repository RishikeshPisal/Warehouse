from django.urls import path,re_path
from .views import *


urlpatterns = [
  # re_path(r'^settings(?:/(?P<notification>[\w-]+))?/$', settings_view, name="settings_view"),
  re_path(r'^crops(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', crop_view, name="crop_view"),
  # re_path(r'^crops/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', crop_view, name="crop_view"),
  re_path(r'^crops/delete(?:/(?P<pk>\d+))?/$', delete_crop, name="delete_crop"),
  
  re_path(r'^units(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', unit_view, name="unit_view"),
  # re_path(r'^units/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', unit_view, name="unit_view"),
  # re_path(r'^units/delete(?:/(?P<pk>\d+))?/$', delete_unit, name="delete_unit"),
  
  re_path(r'^conditions(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', condition_view, name="condition_view"),
  # re_path(r'^conditions/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', condition_view, name="condition_view"),
  re_path(r'^conditions/delete(?:/(?P<pk>\d+))?/$', delete_condition, name="delete_condition"),

  re_path(r'^categories(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', category_view, name="category_view"),
  # re_path(r'^categories/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', category_view, name="category_view"),
  re_path(r'^categories/delete(?:/(?P<pk>\d+))?/$', delete_category, name="delete_category"),

  re_path(r'^insurance(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', insurance_view, name="insurance_view"),
  # re_path(r'^insurance/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', insurance_view, name="insurance_view"),
  re_path(r'^insurance/delete(?:/(?P<pk>\d+))?/$', delete_insurance, name="delete_insurance"),

  re_path(r'^sections(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', section_view, name="section_view"),
  # re_path(r'^sections/update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', section_view, name="section_view"),
  re_path(r'^sections/delete(?:/(?P<pk>\d+))?/$', delete_section, name="delete_section"),

  # path('system/',settings_view,name="settings_view"),

]
