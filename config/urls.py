# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('social_django.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('chat/', include('chat.urls')),
    path('kakaopay/', include('kakaopay.urls', namespace='kakaopay')),
    path('', include('market.urls', namespace='market')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)