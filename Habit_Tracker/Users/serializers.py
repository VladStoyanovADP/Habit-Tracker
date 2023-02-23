from rest_framework import serializers
from .models import Person, Rewards, Habits

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'password', 'email', 'avatar_url',
                  'description', 'created_at', 'currency', 'phone', 'achievements')

class RewardsSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field="id"
    )
    class Meta:
        model = Rewards
        fields = ['rewards_name', 'rewards_description', 'rewards_cost', 'user_id']
        
class HabitsSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.SlugRelatedField(
        read_only=True,
        slug_field="id"
    )
    class Meta:
        model = Habits
        fields = ['habit_name', 'habit_category', 'habit_type', 'habit_streak', 'user_id']