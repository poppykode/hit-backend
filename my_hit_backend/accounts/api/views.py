from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)
from rest_framework.response import Response
from .serializers import RegistrationSerializer, CourseIdSerializer
from accounts.models import User
from accommodation.models import Booking
# from django.conf import settings
# User = settings.AUTH_USER_MODEL 

@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    try:
        qs = User.objects.get(pk=token.user_id)
    except User.DoesNotExist:
        return Response({'error': 'user id does not exist'},status=HTTP_404_NOT_FOUND)
    
    acc = Booking.objects.filter(user=token.user_id).exists()
    return Response({'token': token.key,'user_id': token.user_id,'course_id':qs.course.id,'has_accomodation':acc},status=HTTP_200_OK)
    

@csrf_exempt
@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
@permission_classes((AllowAny,))
def register(request):
    if request.method =='POST':
        qs = User.objects.all()
        email = request.data.get('email')
        username = request.data.get('username')
        for i in qs:
            if username == i.username:
                return Response({'error':'username already exists.'}, status=HTTP_400_BAD_REQUEST) 
            if email == i.email:
                return Response({'error':'email already exists.'}, status=HTTP_400_BAD_REQUEST) 
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET',])
def get_user(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        id = request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(id=id)
            print("User")
            print(queryset)    
            serializer = RegistrationSerializer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def get_user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = RegistrationSerializer(user)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = RegistrationSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(["GET"])
def logout(request):
    print('logout check result')
    print(request.user.auth_token)
    if not request.user.auth_token:
        return Response({'error':'something went wrong'},status= HTTP_404_NOT_FOUND)
    request.user.auth_token.delete()
    return Response({'success':'successfully logout'},status= HTTP_200_OK)



