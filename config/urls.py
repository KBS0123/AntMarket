# config/urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('chat/', include('chat.urls')),  # chat 앱의 URL 패턴을 포함
    path('', include('market.urls', namespace='market')),
]