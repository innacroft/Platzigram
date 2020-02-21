"""post models"""
from django.db import models

# Create your models here.

class User(models.Model):
  """User model"""
  email= models.EmailField(unique=True)
  password= models.CharField(max_length=100)

  first_name=models.CharField(max_length=100)
  last_name=models.CharField(max_length=100)
  country =models.CharField(max_length=100,blank=True)
  city =models.CharField(max_length=100,blank=True)
  is_admin=models.BooleanField(default=False)

  bio= models.TextField(blank=True)
  
  birthdate=models.DateField(blank=True, null=True)
  
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)


def __str__(self):
  """return email"""
  return self.email