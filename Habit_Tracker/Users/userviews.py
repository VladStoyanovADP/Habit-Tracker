from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Person, Rewards, Habits
from Achievements.models import Achievements
from .serializers import PersonSerializer, RewardsSerializer, HabitsSerializer
from Achievements.serializers import AchievementsSerializer

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

# Parametric endpoint requests - rewards - users/:user_id/rewards
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def get_user_rewards(request, user_id):
    queryset = Rewards.objects.filter(user_id=user_id)
    serializer = RewardsSerializer(queryset, many=True, context= {'request': request})
    return Response(serializer.data)

# Parametric endpoint requests - rewards - users/:user_id/rewards/:rewards_id
@api_view(['GET'])
def get_user_rew_id(request, user_id, reward_id):
    queryset = Rewards.objects.get(user_id=user_id, id=reward_id)
    serializer = RewardsSerializer(queryset, context={'request': request})
    return Response(serializer.data) 
    
# Parametric endpoint requests - habits - users/:user_id/habits
@api_view(['GET', 'POST'])
def get_user_habits(request, user_id):
    queryset = Habits.objects.filter(user_id=user_id)
    serializer = HabitsSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)

# Parametric endpoint requests - habits - users/:user_id/habits/:habits_id
@api_view(['GET'])
def get_user_habits_byId(request, user_id, habit_id):
    queryset = Habits.objects.get(user_id=user_id, id=habit_id)
    serializer = HabitsSerializer(queryset, context={'request' : request})
    return Response(serializer.data)

# Parametric endpoint requests - achievements - users/:user_id/achievements/:achievement_id
@api_view(['GET'])
def user_achievements(request, user_id):
    user = Person.objects.get(id=user_id)
    achievements = user.achievements.all()
    serializer = AchievementsSerializer(achievements, many=True)
    return Response(serializer.data)

# Parametric endpoint requests - achievements - users/:user_id/achievements/:achievement_id
@api_view(['GET'])
def user_achiev_id(request, user_id, achievement_id):
    achievement = Achievements.objects.get(id=achievement_id)
    serializer = AchievementsSerializer(achievement)
    return Response(serializer.data)

# Parametric endpoint requests - currency
@api_view(['GET', 'PATCH'])
def user_currency(request, user_id):
    user = Person.objects.get(id=user_id)
    currency = user.currency
    return Response({ 'currency': currency })