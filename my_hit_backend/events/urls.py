from django.urls import path
from .views import (
    delete_event,get_all_events,
    event_details,event_create,
    event_update
    )

app_name='events'
urlpatterns = [
    path('all',get_all_events,name='all'),
    path('delete/<int:pk>',delete_event,name='delete'),
    path('details/<int:pk>',event_details,name='details'),
    path('update/<int:pk>',event_update,name='update'),
    path('create',event_create,name='create'),

]
