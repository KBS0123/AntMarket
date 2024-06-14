from django.urls import path, include
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('update/', views.product_update, name='product_update'),
    path('<str:name>/review/', views.product_review, name='product_review'),
    path('<str:category_slug>/', views.product_list, name='product_list'),
    path('<str:category_slug>/<str:minicategory_slug>/', views.product_list, name='product_list_filtered'),
    path('<str:category_slug>/<str:minicategory_slug>/<str:name>/', views.product_detail, name='product_detail'),
    path('orders/', include('orders.urls', namespace='orders')),
]