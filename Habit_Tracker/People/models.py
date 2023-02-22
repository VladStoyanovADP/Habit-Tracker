from django.db import models
from Achievements.models import Achievements

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
    achievements = models.ManyToManyField(Achievements, related_name='achievement_id')

class Rewards(models.Model):
    rewards_name = models.CharField(max_length = 50)
    rewards_description = models.CharField(max_length = 300)
    rewards_cost = models.IntegerField(default = 0)
    user_id = models.ForeignKey(Person, default = 1, on_delete=models.CASCADE)
    
class Habits(models.Model):
    habit_name = models.CharField(max_length = 100)
    habit_category = models.CharField(max_length = 100)
    habit_type = models.CharField(max_length = 100)
    habit_streak = models.IntegerField(default = 0)
    user_id = models.ForeignKey(Person, default = 1, on_delete=models.CASCADE)