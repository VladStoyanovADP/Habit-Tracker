from rest_framework import viewsets
from .serializers import AchievementsSerializer
from .models import Achievements

class AchievementsViewSet(viewsets.ModelViewSet):
    queryset = Achievements.objects.all()
    serializer_class = AchievementsSerializer
    
