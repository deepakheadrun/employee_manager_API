from django.db import models
from django.contrib.auth.models import User

class Info(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=18,blank=True) 
    mobile= models.CharField(max_length=18,blank=True)
    department=models.CharField(max_length=60,blank=True)
    reporting_to= models.CharField(max_length=60,blank=True)
    date_of_joining =models.DateField(blank=True)
    job_title = models.CharField(max_length=30,blank=True)
    employee_type = models.CharField(max_length=30,blank=True)
    career_goal = models.TextField(blank=True)
    image= models.ImageField(upload_to ='uploads/',blank=True)
    def __str__(self):
        return self.employee_id
   