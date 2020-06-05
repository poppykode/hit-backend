from rest_framework import serializers
from accounts.models import User
from django.conf import settings
from my_hit_backend.utils import StudentNumber
base_url = settings.BASE_URL 

class RegistrationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','image','image_url','email','is_student','student_number','course','password',)

    def get_image_url(self,obj):
        return base_url + obj.image.url

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
        validated_data['password'],first_name=validated_data['first_name'],image =validated_data['image'],last_name=validated_data['last_name'],course=validated_data['course'],
        is_student = True,student_number=StudentNumber())      
        return user

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class CourseIdSerializer(serializers.Serializer):
    user = serializers.CharField(required=True)
