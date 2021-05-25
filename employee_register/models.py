from django.db import models
from datetime import date 
from django.contrib.auth.models import UserManager

import django.utils

import datetime
#from django.utils.timezone import date
# Create your models here.

class Vehicle(models.Model):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=50)

    def __str__(self):
        return self.plate

class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    lattitude = models.CharField(max_length=100)
    longtitude = models.CharField(max_length=3)

    vehicle= models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    datetimeC=models.DateTimeField(default=django.utils.timezone.now,max_length=225,blank=True,null=True)
    
