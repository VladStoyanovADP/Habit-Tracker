from django.urls import path, include
from rest_framework import routers
from Achievements import achviews
from People import userviews



router = routers.DefaultRouter()
router.register(r'users', userviews.PersonViewSet)
router.register(r'rewards', userviews.RewardsViewSet)
router.register(r'habits', userviews.HabitsViewSet)
router.register(r'achievements', achviews.AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:user_id>/habits', userviews.get_user_habits),
    path('users/<int:user_id>/habits/<int:habit_id>', userviews.get_user_habits_byId),
    path('users/<int:user_id>/achievements', achviews.get_user_achievements)
]