from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Person, Rewards, Habits

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 'name', 'username', 'password', 'email', 'avatar_url', 'description', 'created_at', 'currency', 'phone', 'achievements')

class RewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rewards
        fields = ['id', 'rewards_name', 'rewards_description', 'rewards_cost', 'user_id']
        
class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = ['id', 'habit_name', 'habit_category', 'habit_type', 'habit_streak', 'user_id']

class TokenViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token