# config/urls.py 

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('chat/<str:username>/', chat_views.ChatView.as_view(), name='chat'),
    path('', include('market.urls', namespace='market')),
    path('orders/', include('orders.urls', namespace='orders')),
    path('kakaopay/', include('kakaopay.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
