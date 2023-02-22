from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from People.serializers import PersonSerializer
from .serializers import AchievementsSerializer
from .models import Achievements
from People.models import Person, Rewards


class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer
    
@api_view(['GET', 'POST'])
def get_user_achievements(request, user_id):
    queryset = Person.objects.all(Person.achievements)
    serializer = PersonSerializer(queryset, many=True, context={'request': request})
    return Response(serializer.data)