from django.urls import path,re_path
from .views import *


urlpatterns = [
  # path('all/',all_crops_view,name='all_crops_view'),
  re_path(r'^all(?:/(?P<notification>[\w-]+))?/$', all_crops_view, name="all_crops_view"),
  re_path(r'^create(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', add_crop_view, name="add_crop_view"),
  re_path(r'^update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', update_crop_view, name="update_crop_view"),
  re_path(r'^delete(?:/(?P<pk>\d+))?/$', delete_crop, name="delete_crop"),
  re_path(r'^unit(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', add_unit_view, name="add_unit_view"),

]
