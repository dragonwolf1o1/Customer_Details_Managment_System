from django.db import models
from datetime import datetime

# Create your models here.
class Customers_Details(models.Model):
    c_name=models.CharField(max_length=100)
    detail1=models.TextField(max_length=1000)
    detail2=models.TextField(max_length=1000)
    detail3=models.TextField(max_length=1000)
    detail4=models.TextField(max_length=1000)
    date=models.DateField()
    
    def __str__(self):
        return self.c_name