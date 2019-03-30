"""iotTech URL Configuration
style="border:0;font-family:Comic Sans MS, cursive, sans-serif; background: none; display: block; font-weight:bold; margin: 20px auto; text-align: center; border: 2px solid gray; padding: 14px 10px; width: 200px; outline: none; color: white; font-weight:bold; border-radius: 24px;transition: 0.25s;"
"""
from django.contrib import admin
from django.urls import path  ,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('part1.urls')),
    path('register/',include('part1.urls')),
    path('logout/', include('part1.urls')),
    path('loggedin/upload/',include('part1.urls')),
    path('loggedin/files/', include('part1.urls')),
    path('loggedin/profile/', include('part1.urls')),
    path('loggedin/files/<str:usr>/<str:fil>/',include('part1.urls')),
    path('contact/',include('part1.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)