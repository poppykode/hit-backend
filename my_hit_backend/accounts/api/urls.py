from django.urls import path
from .views import (
    login,
    register,
    logout,
    get_user,
    get_user_detail,
    )


urlpatterns = [
    path('login', login),
    path('logout', logout),
    path('register', register),
    path('user', get_user),
    path('get_user_detail/<int:pk>',get_user_detail)
    
]