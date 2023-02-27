from django.db import models
from django.contrib.auth.models import User
from Achievements.models import Achievements


# class User(AbstractUser):
#     username = models.CharField(max_length = 80, unique=True)
#     user_firstname = models.CharField(max_length = 80, blank=True, null=False)
#     user_surname = models.CharField(max_length = 80, blank=True, null=False)
#     # user_password = models.CharField(max_length = 80, default="password123")
#     user_email = models.EmailField(max_length = 80)
    
#     # USERNAME_FIELD = 'username'
#     # REQUIRED_FIELDS = ['user_firstname', 'user_surname']
    
#     def __str__(self):
#         return f"{self.user_email} - {self.user_firstname} {self.user_surname}"
    
class Profile(models.Model):
    user_id = models.OneToOneField(User, default=1,on_delete=models.CASCADE)
    user_avatar_url = models.URLField(max_length = 100, blank=True)
    user_description = models.CharField(max_length = 100, blank=True)
    user_created_at = models.DateTimeField(auto_now_add=True, editable=False)
    user_currency = models.DecimalField(max_digits = 15, decimal_places=2, blank=True, default=0)
    achievements = models.ManyToManyField(Achievements, related_name='user_achievements', blank=True)
    
class Rewards(models.Model):
    rewards_name = models.CharField(max_length = 50)
    rewards_description = models.CharField(max_length = 300)
    rewards_cost = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    
class Habits(models.Model):
    habit_name = models.CharField(max_length = 100)
    habit_category = models.CharField(max_length = 100)
    habit_type = models.CharField(max_length = 100)
    habit_streak = models.IntegerField(default = 0)
    user_id = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)