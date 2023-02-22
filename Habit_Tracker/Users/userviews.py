from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer, RewardsSerializer, HabitsSerializer
from .models import Person, Rewards, Habits

# Classes
class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all().order_by('name')
    serializer_class = PersonSerializer

class RewardsViewSet(viewsets.ModelViewSet):
    queryset = Rewards.objects.all()
    serializer_class = RewardsSerializer
    
class HabitsViewSet(viewsets.ModelViewSet):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer

# Parametric endpoint requests - rewards
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def get_user_rewards(request, user_id):
    queryset = Rewards.objects.filter(user_id=user_id)
    serializer = RewardsSerializer(queryset, many=True, context= {'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_user_rew_id(request, user_id, reward_id):
    queryset = Rewards.objects.get(user_id=user_id, id=reward_id)
    serializer = RewardsSerializer(queryset, context={'request': request})
    return Response(serializer.data) 
    
# Parametric endpoint requests - habits
@api_view(['GET', 'POST'])
def get_user_habits(request, user_id):
    queryset = Habits.objects.filter(user_id=user_id)
    serializer = HabitsSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def get_user_habits_byId(request, user_id, habit_id):
    queryset = Habits.objects.get(user_id=user_id, id=habit_id)
    serializer = HabitsSerializer(queryset, context={'request' : request})
    return Response(serializer.data)
