# config/urls.py 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('chat/', include('chat.urls')),
    path('', include('market.urls', namespace='market')),
    path('orders/', include('orders.urls', namespace='orders')),
]
