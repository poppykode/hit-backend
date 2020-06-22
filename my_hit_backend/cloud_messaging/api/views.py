from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import CloudMessagingSerializer
from cloud_messaging.models import CloudMessaging
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)


@csrf_exempt
@api_view(['POST'])
def fcm_token(request):
    if request.method == 'POST':
        serializer = CloudMessagingSerializer(data=request.data)
        # qs = get_object_or_404(CloudMessaging, user=request.user)
        try:
            qs = CloudMessaging.objects.get(user=request.user)
            if qs and request.data["fcm_token"] == qs.fcm_token:
                return Response({'message': True})
            else:
                qs.delete()
        except CloudMessaging.DoesNotExist:
            print('ma1')
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
