from django.urls import path
from .views import (
    create_meal,
    check_meal,
    get_summary,
    make_payment,
    buy_meal,
)

urlpatterns = [
    path('create', create_meal),
    path('check-meal', check_meal),
    path('get-summary', get_summary),
    path('make-payment', make_payment),
    path('buy-meal', buy_meal),
]
