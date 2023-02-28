from .models import Achievements
from rest_framework import serializers

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = ['achievement_id', 'achievement_name', 'achievement_img_url', 'achievement_description', 'achievement_unlock', 'achievement_reward']