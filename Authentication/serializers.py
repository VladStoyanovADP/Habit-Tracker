from rest_framework import serializers
from Users.models import User

# Registration
class RegistrationSerializer(serializers.ModelSerializer):    
    class Meta:
        model = User
        fields = ('user_firstname', 'user_surname', 'user_email', 'username', 'user_password')

    
    