from django.db import models

# Create your models here.
class Setting(models.Model):
  company_name = models.CharField(max_length=100,null=True)
  rent_per_month = models.IntegerField()
  min_months_for_rent = models.IntegerField(null=True)
  loan_amount_percentage = models.IntegerField()
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)

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

class CropCondition(models.Model):
  name = models.CharField(max_length=100,unique=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()

  def __str__(self):
    return self.name

class CropCategory(models.Model):
  name = models.CharField(max_length=100,unique=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()

  def __str__(self):
    return self.name

class Insurance(models.Model):
  name = models.CharField(max_length=100,unique=True)
  '''
    other details remaining
  '''
  is_deleted = models.BooleanField(default=False)
  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()

  def __str__(self):
    return self.name

class Section(models.Model):
  name = models.CharField(max_length=100,unique=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()

  def __str__(self):
    return self.name