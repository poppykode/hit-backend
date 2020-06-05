from django.urls import path
from .views import accomodation_create,accomodation_list,update_accommodation,accomodation_details,accomodation_delete

app_name='accomodation'
urlpatterns = [
    path('create',accomodation_create,name='accomodation_create'),
    path('all',accomodation_list,name='accomodation_list'),
    path('update/<int:pk>',update_accommodation,name='accomodation_update'),
    path('details/<int:pk>',accomodation_details,name='accomodation_details'),
    path('delete/<int:pk>',accomodation_delete,name='accomodation_delete'),

]
