from django.urls import path
from .views import(
    add_comment,
    all_queries,
    get_query_by_id,
    add_query,
    delete_comment,
    delete_query
    )

app_name='queries'
urlpatterns = [
    path('all',all_queries, name='all_queries'),
    path('add/query',add_query, name='add_query'),
    path('add/comment/<int:pk>',add_comment, name='add_comment'),
    path('get/query/<int:pk>',get_query_by_id, name='get_query_by_id'),
    path('comment/delete/<int:pk>',delete_comment, name='delete_comment'),
    path('query/delete/<int:pk>',delete_query, name='delete_query'),
   
]

