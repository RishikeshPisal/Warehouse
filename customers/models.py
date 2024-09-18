from django.db import models

# Create your models here.
class Customer(models.Model):
  name = models.CharField(max_length=100)
  address = models.CharField(max_length=255)
  city = models.CharField(max_length=100)
  pin_code = models.CharField(max_length=10)
  state = models.CharField(max_length=100)
  contact_number = models.CharField(max_length=15)
  email = models.EmailField(unique=True,null=True)
  time = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.name}"



