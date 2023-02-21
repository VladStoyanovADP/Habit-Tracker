from rest_framework import serializers
from .models import Person, Rewards

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'password', 'email', 'avatar_url', 'description', 'created_at', 'currency', 'phone', 'habits', 'achievements')


class RewardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rewards
        fields = ['rewards_name', 'rewards_description', 'rewards_cost', 'user_id']