from django.urls import path
from .views import query, get_response,get_query,response_enpoint

urlpatterns = [
    path('create',query),
    path('all',get_query),
    path('response',response_enpoint),
    path('response/<int:query_id>',get_response)
]