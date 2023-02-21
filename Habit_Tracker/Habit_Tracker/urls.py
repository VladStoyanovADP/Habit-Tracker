from django.urls import path, include
from rest_framework import routers
from Users.views import get_user_habits
from People import views
from Rewards import views
from Achievements import views



# ***DAN*** was having some weird issues where each router.register is being read as an attribute to one another
# had to comment them out to move on, but might see some slight changes across the views files as I was trying to make them work
 
router = routers.DefaultRouter()
# router.register(r'people', views.PersonViewSet)
# router.register(r'rewards', views.RewardsViewSet)
router.register(r'achievements', views.AchievementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:id>/habits', get_user_habits)
]
