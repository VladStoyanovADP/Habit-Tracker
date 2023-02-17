from rest_framework import serializers
from HabitTracker.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'habit')
