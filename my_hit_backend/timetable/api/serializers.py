from rest_framework import serializers
from timetable.models import Timetable,Course
from django.conf import settings
base_url = settings.BASE_URL 

class TimetableSerializer(serializers.ModelSerializer):
    file_url = serializers.SerializerMethodField('get_file_url')
    file_name = serializers.CharField(source="course.name", read_only=True)
    class Meta:
        model = Timetable
        fields = ('course','file_url','file_name')

    def get_file_url(self,obj):
        return base_url + obj.file_name.url

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id','name',)


