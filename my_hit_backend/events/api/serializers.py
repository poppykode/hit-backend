from rest_framework import serializers
from events.models import Event
from django.conf import settings
base_url = settings.BASE_URL 

class EventsSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Event
        fields = ('id','name','date','description','location','image_url')

    def get_image_url(self,obj):
        return base_url + obj.image.url


