from rest_framework import serializers
from Habits.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'habit')
