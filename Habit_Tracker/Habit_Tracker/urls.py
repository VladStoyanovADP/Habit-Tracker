from django.urls import path, include
from rest_framework import routers
from Users.views import get_user_habits
from People import views
from Rewards import views
from Achievements import views


router = routers.DefaultRouter()
router.register(r'people', views.PersonViewSet)
router.register(r'rewards', views.RewardsViewset)
router.register(r'achievements', views.AchievementsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:id>/habits', get_user_habits)

]

