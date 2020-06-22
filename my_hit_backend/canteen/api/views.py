from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.db.models import F
from .serializers import MealSerializer
from canteen.models import Meal
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT
)


@csrf_exempt
@api_view(['POST'])
def create_meal(request):
    if request.method == 'POST':
        serializer = MealSerializer(data=request.data)
        request.data['user'] = request.user.id
        request.data['total_cost'] = request.data['number_of_meals'] * 20
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['GET', ])
def check_meal(request):
    if request.method == 'GET':
        qs = Meal.objects.filter(user=request.user).exists()
        return Response({'has_meal': qs}, status=HTTP_200_OK)


@csrf_exempt
@api_view(['GET', ])
def get_summary(request):
    if request.method == 'GET':
        qs = Meal.objects.filter(user=request.user)
        serializer = MealSerializer(qs, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    return Response({'error': 'method not allowed.'}, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST', ])
def make_payment(request):
    if request.method == 'POST':
        amt_paid = request.data['amt_paid']
        total_amount = get_object_or_404(Meal, user=request.user)
        if amt_paid >= total_amount.total_cost:
            total_amount.paid = True
            total_amount.save(update_fields=["paid"])
            return Response({'success': 'payment successful'}, status=HTTP_200_OK)
        return Response({'error': 'payment not successful, due to insuffient funds.'}, status=HTTP_400_BAD_REQUEST)
    return Response({'error': 'method not allowed.'}, status=HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(['POST', ])
def buy_meal(request):
    if request.method == 'POST':
        number_of_meals = request.data['number_of_meals']
        _number_of_meals = Meal.objects.get(user=request.user)
        print(type(number_of_meals))
        if number_of_meals <= _number_of_meals.number_of_meals:
            Meal.objects.filter(user=request.user).update(
                number_of_meals=F('number_of_meals') - number_of_meals)
            return Response({'success': 'successfully bought'})
        return Response({'error': 'you only have ' + str(_number_of_meals.number_of_meals) + ' meals left.'})
    return Response({'error': 'method not allowed.'}, status=HTTP_400_BAD_REQUEST)
