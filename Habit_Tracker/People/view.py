from rest_framework import viewsets, permissions
from .serializers import PersonSerializer, RewardsSerializer
from .models import Person, Rewards

# Create your views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer

class RewardsViewset(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    permission_classes = [permissions.IsAuthenticated]