from django.db import models

# Create your models here.
class Crop(models.Model):
  name = models.CharField(max_length=255,unique=True)
  is_deleted = models.BooleanField(default=False)
  time = models.DateTimeField(auto_now=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()
  
  def __str__(self):
    return self.name

class Unit(models.Model):
  name = models.CharField(max_length=25,unique=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()

  def __str__(self):
    return self.name