from django.urls import path, include
from rest_framework import routers
from Achievements import achviews
from People import userviews


router = routers.DefaultRouter()
router.register(r'people', userviews.PersonViewSet)
router.register(r'rewards', userviews.RewardsViewSet)
router.register(r'habits', userviews.HabitsViewSet)
router.register(r'achievements', achviews.AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]