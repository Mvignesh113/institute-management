from django.db import models

# Create your models here.
class students_details(models.Model):
  idnum=models.IntegerField(null=True,blank=True)
  Name=models.CharField(max_length=30, null=True, blank=True)
  Gender=models.CharField(max_length=10, null=True, blank=True)
  course=models.CharField(max_length=20,null=True,blank=True)
  duration=models.CharField(max_length=10,null=True,blank=True)
  phnum=models.BigIntegerField(null=True,blank=True)
  place=models.CharField(max_length=30,null=True,blank=True)
  paidfees=models.IntegerField(null=True,blank=True)
  paiddate=models.DateTimeField(auto_now_add=True)
  total_fees = models.FloatField(default=0.0)  # Add total fees field
  pendingfees=models.IntegerField(null=True,blank=True)


class course(models.Model):
 coursename=models.CharField(max_length=50, null=True,blank=True)
 coursefees=models.IntegerField(null=True,blank=True)


 
  
  
  