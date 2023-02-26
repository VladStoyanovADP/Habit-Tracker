from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenViewSerializer, RegistrationSerializer
# from Users.serializers import 
import uuid

# Registration 
##
class RegistrationAPIView(generics.GenericAPIView):
    
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        
        
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "Request_id": str(uuid.uuid4()),
                "Message": "Registration Successful",
                
                "Person": serializer.data}, status= status.HTTP_201_CREATED
                )
            
        return Response({"Errors": serializer.errors}, status= status.HTTP_400_BAD_REQUEST)
    
# Login 


# Logout


class TokenView(TokenObtainPairView):
    serializer_class = TokenViewSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data = {
                'success': True,
                'message': 'Login successful'
            }
        return response