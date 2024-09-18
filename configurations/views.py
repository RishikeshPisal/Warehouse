from django.shortcuts import render
from .forms import SettingsForm
from .models import Setting

# Create your views here.

def settings_view(request):
  settings = Setting.objects.first()
  form = SettingsForm(instance=settings)
  notification = None
  if request.method == 'POST':
    form = SettingsForm(data=request.POST,instance=settings)
    if form.is_valid():
      form.save()
      notification = 'success'
    else:
      notification = 'failed'


  return render(request, 'settings.html',{'form':form,'notification':notification})