from django.db import models

# Create your models here.
class Setting(models.Model):
  company_name = models.CharField(max_length=100,null=True)
  min_months_for_rent = models.IntegerField(null=True)
  loan_amount_percentage = models.IntegerField()
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)

class Crop(models.Model):
  name = models.CharField(max_length=255,unique=True)
  current_market_price = models.DecimalField(max_digits=10,decimal_places=2)
  is_deleted = models.BooleanField(default=False)
  time = models.DateTimeField(auto_now_add=True)

  def save(self, *args, **kwargs):
    self.name = self.name.title()
    return super().save()
  
  def __str__(self):
    return self.name

class Unit(models.Model):
  name = models.CharField(max_length=25,unique=True)
  # value relative to quintal/whichever is considered while putting rent_per_month in Setting
  rent_per_month = models.DecimalField(decimal_places=3,max_digits=10,blank=True,default=0)

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