from django.db import models

# Create your models here.
class Setting(models.Model):
  company_name = models.CharField(max_length=100,null=True)
  rent_per_day = models.IntegerField()
  min_months_for_rent = models.IntegerField(null=True)
  loan_interest = models.DecimalField(decimal_places=2,max_digits=10)
