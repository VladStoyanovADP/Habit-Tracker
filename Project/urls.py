from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from Achievements import achviews
from Users import userviews
from Authentication import authviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from Authentication.authviews import RegistrationAPIView

router = routers.DefaultRouter()
router.register(r'users', userviews.PersonViewSet)
router.register(r'rewards', userviews.RewardsViewSet)
router.register(r'habits', userviews.HabitsViewSet)
router.register(r'achievements', achviews.AchievementsViewSet)

urlpatterns = [
    #base
    path('', include(router.urls)),
    #user-rewards
    path('users/<int:user_id>/rewards', userviews.get_user_rewards),
    path('users/<int:user_id>/rewards/<int:reward_id>', userviews.get_user_rew_id),
    #user-habits
    path('users/<int:user_id>/habits', userviews.get_user_habits),
    path('users/<int:user_id>/habits/<int:habit_id>', userviews.get_user_habits_byId),
    #user-achievements
    path('users/<int:user_id>/achievements', userviews.user_achievements),
    path('users/<int:user_id>/achievements/<int:achievement_id>', userviews.user_achiev_id),
    #user-currency
    path('users/<int:user_id>/currency', userviews.user_currency),
    #authentication
    # path('register/', RegistrationAPIView.as_view(), name='register'),
    # path('userlogin/', TokenObtainPairView.as_view(), name='login')
    # path('refresh-token/', TokenRefreshView.as_view(), name='refreshtoken')
    #notsureifwork
    # path('login', authviews.as_view(), name='token_obtain'),
    # path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]