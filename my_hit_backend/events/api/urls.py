from django.urls import path
from .views import get_events,get_event_by_id

urlpatterns = [
    path('all',get_events),
    path('',get_event_by_id),
]