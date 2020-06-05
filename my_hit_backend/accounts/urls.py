from django.urls import path
from .views import (
    login_view,
    login,
    users,
    toggle_fees_status,
)

app_name='accounts'
urlpatterns = [
    path('login/view/', login_view,name='login_view'),
    path('login/', login,name='login'),
    path('users/', users,name='users'),
    path('toggle/<int:pk>', toggle_fees_status,name='toggle'),

]
