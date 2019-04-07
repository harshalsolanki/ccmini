from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(primary_key=True,max_length=100)
	password = models.CharField(max_length = 100)
	first = models.CharField(max_length=100)
	last = models.CharField(max_length=100)
	email = models.EmailField(max_length=100,blank=False)
	tours = models.CharField(max_length=500)
	
	
