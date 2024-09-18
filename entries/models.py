from django.db import models
from customers.models import Customer
from crops.models import *
from configurations.models import Setting
from datetime import datetime
# Create your models here.
class Entry(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
  sacks = models.IntegerField()
  weight = models.IntegerField()
  unit = models.ForeignKey(Unit, on_delete=models.PROTECT)
  price_per_unit = models.IntegerField()
  rent_per_day = models.IntegerField()
  rent_paid = models.IntegerField(default=0)
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)
  arrival_time = models.DateTimeField(auto_now=True)
  departure_time = models.DateTimeField(null=True)
  closed = models.BooleanField(default=False)
  def __str__(self):
    return f"{self.customer.name} - {self.crop.name}"
  
  def get_total_rent(self):
    min_months = Setting.objects.first().min_months_for_rent
    if self.closed:
      days = (self.departure_time-self.arrival_time).days
    else:
      days = (datetime.now()-self.arrival_time).days
    return max(
      days*self.rent_per_day*self.sacks,
      self.rent_per_day*30*min_months*self.sacks
    )

  def get_due_rent(self):
    return self.get_total_rent() - self.rent_paid

  def get_total_price(self):
    return self.price_per_unit*self.weight

  def save(self, *args, **kwargs):
    if self.pk is None: # if the object is being created
      self.rent_per_day = Setting.objects.first().rent_per_day
      self.loan_interest = Setting.objects.first().loan_interest
    
    return super().save(*args, **kwargs)

