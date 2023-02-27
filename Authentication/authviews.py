from rest_framework import generics
from rest_framework.response import Response
from Users.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from Users.models import User
from Users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import status

# Registration
class RegistrationAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": token.key
        })
    
# Login 
class LoginAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token, _ = Token.objects.get_or_create(user=request.user)
        return Response({'token': token.key})

# Logout
class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        Token.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)

