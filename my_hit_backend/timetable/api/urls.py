from django.urls import path
from .views import get_timetable, get_courses

urlpatterns = [
    path('timetable/<int:id>',get_timetable),
    path('courses',get_courses),
]