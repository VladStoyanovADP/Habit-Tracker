from django.urls import path, include
from rest_framework import routers
from Achievements import views as AchievementsViewSet
from People import views



router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'rewards', views.RewardsViewSet)
router.register(r'achievements', AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]