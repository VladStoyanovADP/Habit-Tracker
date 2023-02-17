from rest_framework.response import Response
from rest_framework.decorators import api_view
from HabitTracker.models import Person
from HabitTracker.serializers import PersonSerializer


@api_view(['GET'])
def get_person_data(request):
    queryset = Person.objects.all()
    serializer = PersonSerializer(queryset, many=True)
    return Response(serializer.data)
