# config/urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),  # chat 앱의 URL 패턴을 포함
]