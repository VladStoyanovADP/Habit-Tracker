from rest_framework import serializers
from Users.models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'habit')
