from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializers import MealSerializer
from events.models import Meal
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)


# @csrf_exempt
# @api_view(['POST'])
# def create_meal(request):
#     try:
#         qs = Meal.objects.get(user=request.user)
#         if qs.number_of_meals > 0:
#             return Response({'error': 'You already have a valid meal voucher.'})
#     except Meal.DoesNotExist:
#         serializer = MealSerializer(data=request.data)
#         request.data['total_cost'] = request.data['total_cost'] * 20
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=HTTP_201_CREATED)
#     return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


# @csrf_exempt
# @api_view(['GET'])
# def meal_payment_summary(request):
#     try:
#         qs = Meal.objects.get(user=request.user)
#     except Meal.DoesNotExist:
#         return Response(status=HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = MealSerializer(qs, many=True)
#         return Response(serializer.data)


# @csrf_exempt
# @api_view(['GET'])
# def make_payment(request, meal_id):
#     try:
#         qs = Meal.objects.get(pk=meal_id)
#     except Meal.DoesNotExist:
#         return Response(status=HTTP_404_NOT_FOUND)
