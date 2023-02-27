from rest_framework import serializers
from .models import Profile, Rewards, Habits
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

# Are User & Registration serializer doing anything differently? // serving a purpose

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_firstname', 'user_surname', 'username', 'user_password', 'user_email')
        
class RegistrationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('user_firstname', 'user_surname', 'user_email', 'username', 'user_password')
          
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

