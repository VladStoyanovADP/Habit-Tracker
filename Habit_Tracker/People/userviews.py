from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer, RewardsSerializer, HabitsSerializer
from .models import Person, Rewards, Habits

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer

class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    
class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    
@api_view(['GET'])
def get_user_habits(request, user_id):
    queryset = Habits.objects.filter(user_id=user_id)
    serializer = HabitsSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)
