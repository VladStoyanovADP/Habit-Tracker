from django.db import models

# Create your models here.
class Rewards(models.Model):
    rewards_name = models.CharField(max_length = 50)
    rewards_description = models.CharField(max_length = 300)
    rewards_cost = models.IntegerField(default = 0)