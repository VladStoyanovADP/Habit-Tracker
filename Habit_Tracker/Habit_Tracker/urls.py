from django.urls import path, include
from rest_framework import routers
from People import view
from Users.views import get_user_habits



router = routers.DefaultRouter()
router.register(r'people', view.PersonViewSet)
router.register(r'rewards', view.RewardsViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('users/<int:id>/habits', get_user_habits)
]