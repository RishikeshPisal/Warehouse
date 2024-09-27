from django.db import models
from customers.models import Customer
from configurations.models import *
from datetime import datetime

class Entry(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
  insurance = models.ForeignKey(Insurance,on_delete=models.SET_NULL,null=True)
  unit = models.ForeignKey(Unit,on_delete=models.PROTECT,null=True)
  
  policy_no = models.CharField(max_length=50)
  other_details = models.CharField(max_length=150)
  vehicle_no = models.CharField(max_length=50)
  driver_name = models.CharField(max_length=100)
  # not using foreign key to avoid loosing data on deletion
  crop_condition = models.CharField(max_length=25)
  crop_category = models.CharField(max_length=25)
  section = models.CharField(max_length=25)

  sacks = models.IntegerField()
  weight = models.IntegerField()
  price_per_unit = models.IntegerField()

  rent_per_month = models.DecimalField(max_digits=10,decimal_places=3)
  rent_paid = models.IntegerField(default=0)
  
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)
  interest_paid = models.IntegerField(default=0)
  principle_remaining = models.IntegerField()

  min_months = models.IntegerField()
  arrival_date = models.DateField(auto_now_add=True)
  insurance_till = models.DateField()
  departure_date = models.DateField(null=True,blank=True)
  closed = models.BooleanField(default=False)
  
  def __str__(self):
    return f"{self.customer.name} - {self.crop.name}"
  
  def get_total_rent(self):
    days = self.total_days()
    return max(
      days*self.rent_per_month*self.weight/30,
      self.rent_per_month*self.min_months*self.weight
    )

  def get_due_rent(self):
    return self.get_total_rent() - self.rent_paid

  def get_total_interest(self):
    days = self.total_days()
    print(days,self.loan_interest,self.principle_remaining)
    return (self.principle_remaining*self.loan_interest*days)/100
  
  def get_due_interest(self):
    return self.get_total_interest() - self.interest_paid
  
  def get_total_price(self):
    return self.price_per_unit*self.weight

  def total_days(self):
    if self.closed:
      days = (self.departure_date-self.arrival_date).days
    else:
      days = (datetime.now().date()-self.arrival_date).days
    return days
  
  def save(self, *args, **kwargs):
    if self.pk is None: # if the object is being created
      self.min_months = Setting.objects.first().min_months_for_rent
      self.loan_interest = Setting.objects.first().loan_interest
      self.rent_per_month = self.unit.rent_per_month
    
    return super().save(*args, **kwargs)


class PaymentHistory(models.Model):
  TYPE = (
    (1,'Rent'),
    (2,'Interest')
  )
  entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
  amount = models.IntegerField()
  time = models.DateTimeField(auto_now_add=True)
  type = models.CharField(max_length=5,choices=TYPE)



class Outward(models.Model):
  rent_history = models.ForeignKey(Entry,on_delete=models.CASCADE)
  sacks = models.IntegerField()
