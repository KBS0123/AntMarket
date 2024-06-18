# kakaopay/urls.py
from django.urls import path
from . import views

app_name = "kakaopay"

urlpatterns = [
    path('', views.index, name='index'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('fail/', views.fail, name='fail'),
 ]

