from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'username', 'password', 'email', 'avatar_url', 'description', 'created_at', 'currency', 'phone', 'habits', 'achievements')