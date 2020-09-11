from django.db import models
from django.contrib.auth.models import User
import datetime

class Experience(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60,blank=True) 
    job_title = models.CharField(max_length=30,blank=True)
    _from =models.DateField(blank=True,default=datetime.date.today)
    _to =models.DateField(blank=True,default=datetime.date.today)
    description= models.CharField(max_length=300,blank=True)
    