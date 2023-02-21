from django.urls import path, include
from rest_framework import routers
from Users.views import get_user_habits
from People import views as PersonViewSet
from People import views as RewardsViewSet
from Achievements import views as AchievementsViewSet

router = routers.DefaultRouter()
router.register(r'people', PersonViewSet)
router.register(r'rewards', RewardsViewSet)
router.register(r'achievements', AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:id>/habits', get_user_habits)

]

