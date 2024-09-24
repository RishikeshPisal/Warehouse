from django.urls import path,re_path
from .views import *


urlpatterns = [
  re_path(r'^create(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', add_customer_view, name="add_customer_view"),
  re_path(r'^update(?:/(?P<pk>\d+))?(?:/(?P<notification>[\w-]+))?/$', update_customer_view, name="update_customer_view"),

]
