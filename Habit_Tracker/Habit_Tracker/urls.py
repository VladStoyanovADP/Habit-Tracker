from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from Achievements import achviews
from Users import userviews
from Users.userviews import TokenView



router = routers.DefaultRouter()
router.register(r'users', userviews.PersonViewSet)
router.register(r'rewards', userviews.RewardsViewSet)
router.register(r'habits', userviews.HabitsViewSet)
router.register(r'achievements', achviews.AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:user_id>/rewards', userviews.get_user_rewards),
    path('users/<int:user_id>/rewards/<int:reward_id>', userviews.get_user_rew_id),
    path('users/<int:user_id>/habits', userviews.get_user_habits),
    path('users/<int:user_id>/habits/<int:habit_id>', userviews.get_user_habits_byId),
    path('users/<int:user_id>/achievements', userviews.user_achievements),
    path('users/<int:user_id>/achievements/<int:achievement_id>', userviews.user_achiev_id),
    path('users/<int:user_id>/currency', userviews.user_currency),
    path('login', TokenView.as_view(), name='token_obtain'),
]