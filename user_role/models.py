from django.db import models
from django.contrib.auth.models import User
class Role(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class UserRole(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    roleid = models.ForeignKey(Role, on_delete=models.CASCADE)
    def __str__(self):
        return self.userid