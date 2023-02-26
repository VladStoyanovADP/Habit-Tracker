from django.db import models

class Achievements(models.Model):
    achievement_name = models.CharField(max_length = 100)
    achievement_img_url = models.URLField(max_length=300)
    achievement_description = models.CharField(max_length=300)
    achievement_unlock = models.BooleanField(default=False)
    achievement_reward = models.DecimalField(max_digits = 15, decimal_places=2)
