from django.urls import path, include
from rest_framework import routers
from Achievements import views
from People import view



router = routers.DefaultRouter()
router.register(r'people', view.PersonViewSet, basename='users')
router.register(r'rewards', view.RewardsViewSet, basename='rewards')
router.register(r'achievements', views.AchievementsViewSet, basename='achievements')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]