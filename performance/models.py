from django.db import models
from django.contrib.auth.models import User

class Performance(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    month = models.CharField(max_length=18,blank=True) 
    rating= models.CharField(max_length=18,blank=True)
    
    def __str__(self):
        return self.month
