from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from Users.models import Person

# Registration 
## Person model used to generate user account
### Any details entered here are required, in model remaining properties need to be set to optional

class RegistrationSerializer(serializers.ModelSerializer):
    
    email = serializers.EmailField(max_length=80, min_length=10)
    username = serializers.CharField(max_length=80, min_length=8)
    password = serializers.CharField(max_length=80, write_only=True)
    
    class Meta:
        model = Person
        fields = ('name', 'email', 'username', 'password')
        
        def validate(self, args):
            email = args.get('email', None)
            username = args.get('username', None)
            if Person.objects.filter(email=email).exists():
                raise serializers.ValidationError('Email already in use')
            if Person.objects.filter(username=username).exists():
                raise serializers.ValidationError('Username already in use')

            return super().validate(args)
        
        def create(self, validated_data):
            pass

# Login 

# Logout

class TokenViewSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['email'] = user.email
        return token
    
    