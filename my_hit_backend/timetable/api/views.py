from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import TimetableSerializer, CourseSerializer
from timetable.models import Timetable,Course

@csrf_exempt
@api_view(['GET'])
def get_timetable(request,id):
    if request.method =='GET':
        qs = Timetable.objects.filter(course=id)
        serializer = TimetableSerializer(qs, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
@permission_classes((AllowAny,))
def get_courses(request):
    if request.method =='GET':
        qs = Course.objects.all()
        serializer = CourseSerializer(qs, many=True)
        return Response(serializer.data)





