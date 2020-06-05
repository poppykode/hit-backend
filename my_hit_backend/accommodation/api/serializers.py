from rest_framework import serializers
from accommodation.models import Booking,Accomodation

class BookingSerializer(serializers.ModelSerializer):
    student_number = serializers.CharField(source='user.student_number', read_only=True)
    price = serializers.CharField(source='accomodation.price', read_only=True)
    accomodation_name = serializers.CharField(source='accomodation.name', read_only=True)
    class Meta:
        model = Booking
        fields = ('id','user','accomodation','timestamp','accomodation_name','price','student_number')

class AccomodationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomodation
        fields = ('id','name','price','available_spaces')


