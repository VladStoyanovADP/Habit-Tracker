from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length = 80)
    username = models.CharField(max_length = 80)
    password = models.CharField(max_length = 80)
    email = models.EmailField(max_length = 80)
    avatar_url = models.URLField(max_length = 100)
    description = models.CharField(max_length = 100)
    created_at = models.CharField(max_length = 20)
    currency = models.DecimalField(max_digits = 15, decimal_places=2)
    phone = models.CharField(max_length = 20)
    habits = models.JSONField()
    achievements = models.JSONField()