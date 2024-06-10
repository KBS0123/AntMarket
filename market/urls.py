from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('update/', views.product_update, name='product_update'),
    path('<str:category_slug>/<str:minicategory_slug>/', views.product_list, name='product_list'),
    path('<str:category_slug>/<str:minicategory_slug>/<str:slug>/', views.product_detail, name='product_detail'),
]