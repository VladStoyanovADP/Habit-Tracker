from rest_framework import serializers
from .models import User, Profile, Rewards, Habits
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_firstname', 'user_surname', 'username', 'user_password', 'user_email')
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user_id', 'user_avatar_url', 'user_description', 'user_created_at', 'user_currency', 'achievements')

class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = ('rewards_name', 'rewards_description', 'rewards_cost', 'user_id')
        
class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ('habit_name', 'habit_category', 'habit_type', 'habit_streak', 'user_id')

