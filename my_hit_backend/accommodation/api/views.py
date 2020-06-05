from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_409_CONFLICT
)
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import F
from .serializers import BookingSerializer,AccomodationSerializer
from accommodation.models import Booking, Accomodation
from accounts.models import User

@csrf_exempt
@api_view(['POST'])
def book(request):
    if request.method =='POST':
        user = request.data.get('user')
        accomodation = request.data.get('accomodation')   
        try:
            qs = Booking.objects.get(user=user)
            return Response({'error':'you have already booked, un-book if you want to choose a different domitory.'},status=HTTP_409_CONFLICT)
        except Booking.DoesNotExist:
            serializer = BookingSerializer(data=request.data)
            is_available = get_object_or_404(Accomodation,id=accomodation)
            has_paid = get_object_or_404(User,pk=user)
            if has_paid.paid == False:
                return Response({'error':'Please make your payment first before attempting to make a booking.'})
            if is_available.available_spaces <= 0:
                return Response({'error':'Accommodation in {} is full.'.format(is_available.name)})
            if serializer.is_valid():
                serializer.save()
                Accomodation.objects.filter(id=accomodation).update(available_spaces=F('available_spaces')-1)
                return Response({'success':'You have successfully booked for accomodation.'}, status=HTTP_201_CREATED) 
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET',])
def get_booking_by_user_id(request):
    if request.method == 'GET':
        queryset = Booking.objects.all()
        user_id = request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(user=user_id)
            serializer = BookingSerializer(queryset ,many=True)
        return Response(serializer.data)
    return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def get_accomodation_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        book = Booking.objects.get(pk=pk)
    except Booking.DoesNotExist:
        return Response(status=HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookingSerializer(book)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = BookingSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        Accomodation.objects.filter(pk=book.accomodation.pk).update(available_spaces=F('available_spaces')+1)
        return Response(status=HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET',])
def get_all_accommodation(request):
    if request.method == 'GET':
        qs = Accomodation.objects.all()
        serializer = AccomodationSerializer(qs,many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET',])
def has_booking (request,user_id):
    qs = Booking.objects.filter(user=user_id).exists()
    return Response({'has_accomodation':qs},status=HTTP_200_OK)
