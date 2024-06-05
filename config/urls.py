# config/urls.py 

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('', include('market.urls', namespace='market')),
    path('chat/', include('chat.urls')),
]