from django.db import models
from customers.models import Customer
from configurations.models import *
from datetime import datetime
from math import floor
class Entry(models.Model):
  customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
  crop = models.ForeignKey(Crop,on_delete=models.CASCADE)
  insurance = models.ForeignKey(Insurance,on_delete=models.SET_NULL,null=True)
  unit = models.ForeignKey(Unit,on_delete=models.PROTECT,null=True)
  
  other_details = models.CharField(max_length=150,null=True,blank=True)
  vehicle_no = models.CharField(max_length=50)
  driver_name = models.CharField(max_length=100)
  # not using foreign key to avoid loosing data on deletion
  crop_condition = models.CharField(max_length=25)
  crop_category = models.CharField(max_length=25)
  section = models.CharField(max_length=25)

  initial_sacks = models.IntegerField()
  sacks = models.IntegerField()
  
  initial_weight = models.IntegerField()
  weight = models.IntegerField()
  price_per_unit = models.IntegerField()
  last_weight_change_date = models.DateField(null=True,blank=True)

  #rent
  rent_per_month = models.DecimalField(max_digits=10,decimal_places=3)
  rent_paid = models.IntegerField(default=0)
  rent_till_last_outward =models.IntegerField(default=0)
  
  #loan and interest
  daily_interest_percentage = models.DecimalField(decimal_places=2,max_digits=10)
  total_principle = models.IntegerField(default=0)
  remaining_principle = models.IntegerField()
  last_principle_date = models.DateField(null=True,blank=True)
  interest_paid = models.IntegerField(default=0)
  interest_till_last_outward = models.IntegerField(default=0)

  #extra charges
  miscellaneous_charges = models.IntegerField(default=0)
  femication_charges = models.IntegerField(default=0)

  #dates
  min_months = models.IntegerField()
  arrival_date = models.DateField(auto_now_add=True)
  departure_date = models.DateField(null=True,blank=True)
  insurance_till = models.DateField()
  closed = models.BooleanField(default=False)
  
  def __str__(self):
    return f"{self.customer.name} - {self.crop.name}"
  
  def get_initial_total_price(self):
    return self.price_per_unit*self.initial_weight
  
  def get_current_total_price(self):
    return self.price_per_unit*self.weight

  def days_since(self,date:datetime=None):
    return ((datetime.now().date() if not self.closed else self.departure_date) - date).days
      
  # calculation functions
  def rent_from_last_outward(self):
    total_days = self.days_since(self.arrival_date)
    days = self.days_since(self.last_weight_change_date)
    if total_days > self.min_months*30:
      return floor(days*self.rent_per_month*self.weight/30)
      
    else:
        return floor(self.rent_per_month*self.min_months*self.weight)

  def interest_from_last_principle(self):
    total_days = self.days_since(self.arrival_date)
    days = self.days_since(self.last_principle_date)
    if total_days > self.min_months*30:
      return floor((self.remaining_principle*self.daily_interest_percentage*days)/100)
    else:
      return floor((self.remaining_principle*self.daily_interest_percentage*self.min_months*30)/100)

  def total_pending_rent(self):
    return self.rent_from_last_outward() + self.rent_till_last_outward - self.rent_paid

  def total_pending_interest(self):
    return self.interest_from_last_principle() + self.interest_till_last_outward - self.interest_paid
  
  def total_days(self):
    if self.closed:
      days = (self.departure_date-self.arrival_date).days
    else:
      days = (datetime.now().date()-self.arrival_date).days
    return days
  
  def save(self, *args, **kwargs):
    if self.pk is None: # if the object is being created
      setting = Setting.objects.first()
      self.min_months = setting.min_months_for_rent
      self.daily_interest_percentage = setting.daily_interest_percentage
      self.rent_per_month = self.unit.rent_per_month
      self.weight = self.initial_weight
      self.sacks = self.initial_sacks
      self.remaining_principle = self.total_principle
      self.last_principle_date = datetime.now()
      self.last_weight_change_date = datetime.now()

    return super().save(*args, **kwargs)


class PaymentHistory(models.Model):
  TYPE = (
    (1,'Rent'),
    (2,'Interest'),
    (3,'Principle'),
    (4,'All'),
  )
  entry = models.ForeignKey(Entry,on_delete=models.CASCADE)
  rent = models.IntegerField(default=0)
  interest = models.IntegerField(default=0)
  principle = models.IntegerField(default=0)
  time = models.DateTimeField(auto_now_add=True)
  type = models.CharField(max_length=25,choices=TYPE)



class Outward(models.Model):
  payment_history = models.ForeignKey(PaymentHistory,on_delete=models.CASCADE)
  sacks = models.IntegerField(blank=True,null=True)
  weight = models.IntegerField()
