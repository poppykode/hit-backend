from django.urls import path
from .views import fcm_token

urlpatterns = [
    path('create', fcm_token),
]
