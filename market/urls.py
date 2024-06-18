from django.urls import path
from . import views

app_name = 'market'

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('<str:category_slug>/create/', views.product_create, name='product_create'),
    path('<str:category_slug>/<str:minicategory_slug>/<int:id>/update/', views.product_update, name='product_update'),
    path('<str:category_slug>/<str:minicategory_slug>/<int:id>/delete/', views.product_delete, name='product_delete'),
    path('<str:category_slug>/', views.product_list, name='product_list'),
    path('<str:category_slug>/<str:minicategory_slug>/', views.product_list, name='product_list_filtered'),
    path('<str:category_slug>/<str:minicategory_slug>/<int:id>/', views.product_detail, name='product_detail'),
]