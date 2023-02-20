from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=80)
    username = models.CharField(max_length=50)
    habit = models.CharField(max_length=50)