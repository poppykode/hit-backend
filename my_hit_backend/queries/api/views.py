from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import QuerySerializer,ResponseSerializer
from queries.models import Query,Comment
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)

@csrf_exempt
@api_view(['POST'])
def query(request):
    if request.method =='POST':
        serializer = QuerySerializer(data=request.data)
        request.data['created_by'] = request.user.id
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_query(request):
    if request.method =='GET':
        qs = Query.objects.filter(student=request.user.id).prefetch_related('created_by')
        serializer = QuerySerializer(qs, many=True)
    return Response(serializer.data)


@csrf_exempt
@api_view(['POST'])
def response_enpoint(request):
    if request.method =='POST':
        serializer = ResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
def get_response(request,query_id):
    if request.method =='GET':
        qs = Comment.objects.filter(query=query_id)
        serializer = ResponseSerializer(qs, many=True)
        return Response(serializer.data)





