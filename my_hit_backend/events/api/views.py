from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import EventsSerializer
from events.models import Event
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)

@csrf_exempt
@api_view(['GET'])
def get_events(request):
    if request.method =='GET':
        qs = Event.objects.all()
        serializer = EventsSerializer(qs, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET',])
def get_event_by_id(request):
    if request.method == 'GET':
        queryset = Event.objects.all()
        id = request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)   
            serializer = EventsSerializer(queryset ,many=True)
        return Response(serializer.data,status = HTTP_200_OK)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)






