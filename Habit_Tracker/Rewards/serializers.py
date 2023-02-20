from django.contrib.auth.models import Rewards
from rest_framework import serializers

class RewardsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rewards
        fields = ['rewards_name', 'rewards_description', 'rewards_cost']

