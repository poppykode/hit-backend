from rest_framework import serializers
from cloud_messaging.models import CloudMessaging


class CloudMessagingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudMessaging
        fields = ('id', 'user', 'fcm_token')

