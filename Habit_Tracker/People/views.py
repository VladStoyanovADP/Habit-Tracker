from rest_framework import viewsets, permissions
from .serializers import PersonSerializer, RewardsSerializer, HabitsSerializer
from .models import Person, Rewards, Habits

# Create views here.
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer

class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [permissions.IsAuthenticated]