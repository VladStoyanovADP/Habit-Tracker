from rest_framework.response import Response
from rest_framework.decorators import api_view
from Users.models import Person
from Habit_Tracker.serializers import PersonSerializer

# Create your views here.

@api_view(['GET'])
def get_user_habits(request, id):
    queryset = Person.objects.get(id=id)
    serializer = PersonSerializer(queryset)
    return Response(serializer.data)