from django.db import models

# Create your models here.

class User(models.Model):
  fullName= models.CharField(max_length=30,blank=True, null=True)
  age = models.CharField(max_length=30,blank=True, null=True)
  telephone = models.CharField(max_length=15,blank=True, null=True)
  email = models.EmailField(max_length=50,blank=True, null=True)
  image = models.CharField(max_length=1500, blank=True, null=True)
  userName = models.CharField(max_length=30, blank=True, null=True)
  
