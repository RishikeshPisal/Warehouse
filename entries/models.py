from django.db import models
from customers.models import Customer
from configurations.models import *
from datetime import datetime

class Entry(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
  insurance = models.ForeignKey(Insurance,on_delete=models.SET_NULL,null=True)
  
  policy_no = models.CharField(max_length=50)
  other_details = models.CharField(max_length=150)
  vehicle_no = models.CharField(max_length=50)
  driver_name = models.CharField(max_length=100)
  # not using foreign key to avoid loosing data on deletion
  unit = models.CharField(max_length=25)
  crop_condition = models.CharField(max_length=25)
  crop_category = models.CharField(max_length=25)
  section = models.CharField(max_length=25)

  sacks = models.IntegerField()
  weight = models.IntegerField()
  price_per_unit = models.IntegerField()

  rent_per_month = models.IntegerField()
  rent_paid = models.IntegerField(default=0)
  
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)
  loan_paid = models.IntegerField(default=0)

  min_months = models.IntegerField()
  arrival_time = models.DateTimeField(auto_now=True)
  insurance_till = models.DateField()
  departure_time = models.DateTimeField(null=True,blank=True)
  closed = models.BooleanField(default=False)
  
  def __str__(self):
    return f"{self.customer.name} - {self.crop.name}"
  
  def get_total_rent(self):
    if self.closed:
      days = (self.departure_time-self.arrival_time).days
    else:
      days = (datetime.now()-self.arrival_time).days
    return max(
      days*self.rent_per_month*self.sacks/30,
      self.rent_per_month*self.min_months*self.sacks
    )

  def get_due_rent(self):
    return self.get_total_rent() - self.rent_paid

  def get_total_interest(self):
    rate_of_interest = self.loan_interest
    total_amount = self.price_per_unit*self.weight
    return (total_amount*rate_of_interest)/100
  
  def get_due_interest(self):
    return self.get_total_interest() - self.loan_paid
  
  def get_total_price(self):
    return self.price_per_unit*self.weight

  def total_days(self):
    if self.closed:
      days = (self.departure_time-self.arrival_time).days
    else:
      days = (datetime.now()-self.arrival_time).days
    return days
  def save(self, *args, **kwargs):
    if self.pk is None: # if the object is being created
      self.min_months = Setting.objects.first().min_months_for_rent
      self.rent_per_month = Setting.objects.first().rent_per_month
      self.loan_interest = Setting.objects.first().loan_interest
    
    return super().save(*args, **kwargs)


class PaymentHistory(models.Model):
  TYPE = (
    (1,'Rent'),
    (2,'Interest')
  )
  entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
  amount = models.IntegerField()
  time = models.DateTimeField(auto_now=True)
  type = models.CharField(max_length=5,choices=TYPE)



class Outward(models.Model):
  rent_history = models.ForeignKey(Entry,on_delete=models.CASCADE)
  sacks = models.IntegerField()
