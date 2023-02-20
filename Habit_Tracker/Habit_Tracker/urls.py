from django.urls import path, include
from Rewards import views
from Users.models import Person
from Users.views import get_user_habits
from Habit_Tracker.serializers import PersonSerializer
from rest_framework import routers, viewsets



router = routers.DefaultRouter()
router.register(r'rewards', views.RewardsViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('users/', get_person_data, name='get_person_data'),
    path('users/<int:id>/habits', get_user_habits)

]
