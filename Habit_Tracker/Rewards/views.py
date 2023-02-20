from Rewards.models import Rewards
from rest_framework import viewsets
from rest_framework import permissions
from Rewards.serializers import RewardsSerializer
# Create your views here.
class RewardsViewset(viewsets.ModelViewSet):
    queryset= Rewards.objects.all()
    serializer_class = RewardsSerializer
    permission_classes = [permissions.IsAuthenticated]