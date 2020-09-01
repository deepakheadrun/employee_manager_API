from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(blank=True)
    by = models.CharField(max_length=60,blank=True)
    description= models.CharField(max_length=500,blank=True)
    
    
