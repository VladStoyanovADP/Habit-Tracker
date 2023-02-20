from django.urls import path, include
from rest_framework import routers
from Rewards import views



router = routers.DefaultRouter()
router.register(r'rewards', views.RewardsViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
