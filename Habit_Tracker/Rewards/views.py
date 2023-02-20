from Rewards.models import Rewards
from rest_framework import viewsets
from rest_framework import permissions
from rewards.serializers import RewardsSerializers
# Create your views here.
class RewardsViewset(viewsets.ModelViewSet):
    queryset= Rewards.objects.all()
    serializer_class = RewardsSerializers
    permission_classes = [permissions.IsAuthenticated]