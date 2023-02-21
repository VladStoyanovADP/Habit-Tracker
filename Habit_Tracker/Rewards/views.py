from rest_framework import viewsets
from .models import Rewards
from .serializers import RewardsSerializer

class RewardsViewSet(viewsets.ModelViewSet):
    queryset= Rewards.objects.all()
    serializer_class = RewardsSerializer
