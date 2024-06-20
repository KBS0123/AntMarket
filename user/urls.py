#user\urls.py
from django.conf import settings
from django.conf .urls.static import static
from django.urls import path
from django.contrib.auth import  views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/#', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('my_products/', views.my_products, name='my_products'),
    path('my_products/<str:category_slug>/', views.my_products, name='my_product_list_filtered'),
    path('delete/', views.UserDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
