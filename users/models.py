from pyexpat import model
from tkinter.tix import INTEGER
from django.db import models

# Create your models here.


class User(models.Model):
    
    userid = models.BigIntegerField(null=False)
    username = models.CharField(max_length=36, null=False)
    password = models.CharField(max_length=64, null=False)
    firstname = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    addressLine1 = models.CharField(max_length=256)
    addressLine2 = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=6)
    state = models.CharField(max_length=2)
        


