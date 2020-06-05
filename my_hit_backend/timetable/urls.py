from django.urls import path
from .views import all_timetables,upload_time,timetable_update,timetable_delete

app_name='timetable'
urlpatterns = [
    path('all',all_timetables,name='all'),
    path('upload',upload_time,name='upload_time'), 
    path('update/<int:pk>',timetable_update,name='timetable_update'), 
    path('delete/<int:pk>',timetable_delete,name='timetable_delete'), 
]

