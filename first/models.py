from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class data(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    mobile=models.CharField(max_length=20)
    dob=models.CharField(max_length=50)
    password=models.CharField(max_length=100)
    gender=models.CharField(max_length=50)

def __str__(self):
    return self.name

class content(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.TextField()
    Datetime = models.DateTimeField(auto_now= True)
def __str__(self):
    return self.title

    