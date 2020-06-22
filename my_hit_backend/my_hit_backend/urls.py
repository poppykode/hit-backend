"""my_hit_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import login_view

urlpatterns = [
    path('', login_view, name="login_view"),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
    path('accounts/p/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('queries/', include('queries.urls')),
    path('events/', include('events.urls')),
    path('timetable/', include('timetable.urls')),
    path('accommodation/', include('accommodation.urls')),
    # APIs
    path('api/v1/course/', include('timetable.api.urls')),
    path('api/v1/accounts/', include('accounts.api.urls')),
    path('api/v1/events/', include('events.api.urls')),
    path('api/v1/accomodation/', include('accommodation.api.urls')),
    path('api/v1/query/', include('queries.api.urls')),
    path('api/v1/fcm/', include('cloud_messaging.api.urls')),
    path('api/v1/canteen/', include('canteen.api.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
