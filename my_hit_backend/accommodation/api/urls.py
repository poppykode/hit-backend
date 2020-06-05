from django.urls import path
from .views import (book, get_accomodation_detail,
                    get_booking_by_user_id, get_all_accommodation,has_booking)

urlpatterns = [
    path('book', book),
    path('get_accomodation_detail/<int:pk>', get_accomodation_detail),
    path('has_booking/<int:user_id>', has_booking),
    path('get_booking_by_user_id', get_booking_by_user_id),
    path('get_all_accommodation',get_all_accommodation)
]
