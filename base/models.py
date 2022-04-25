from django.db import models

# Create your models here.

class Tour(models.Model):
    tour_name = models.CharField(max_length=200)
    price = models.IntegerField(int)
    rating= models.IntegerField(int)
    registred = models.DateTimeField(auto_now_add=True)

class User(models.Model):
    user_name = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    