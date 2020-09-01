from django.db import models
from django.contrib.auth.models import User

class Experience(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=60,blank=True) 
    job_title = models.CharField(max_length=30,blank=True)
    _from =models.DateField(blank=True)
    _to =models.DateField(blank=True)
    description= models.CharField(max_length=300,blank=True)
    