from django.db import models

# Create your models here.

class User(models.Model):
  fullName= models.CharField(max_length=30)
  birthDate = models.DateField()
  telephone = models.CharField(max_length=15)
  email = models.EmailField(max_length=50)
  image = models.CharField(max_length=1500)
  userName = models.CharField(max_length=30, unique=True)
  
