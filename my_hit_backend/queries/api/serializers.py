from rest_framework import serializers
from queries.models import Query,Comment
from django.conf import settings
base_url = settings.BASE_URL 

class QuerySerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source="created_by", read_only=True)
    image_url = serializers.SerializerMethodField('get_image_url')
    class Meta:
        model = Query
        fields = ('id','department','student','title','query_description','timestamp','created_by','fullname','image_url')

    def get_image_url(self,obj):
        return base_url + obj.created_by.image.url

class ResponseSerializer(serializers.ModelSerializer):
    fullname = serializers.CharField(source="commentator", read_only=True)
    class Meta:
        model = Comment
        fields = ('id','query','commentator','reply_message','fullname')


