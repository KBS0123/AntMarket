# market/forms.py

from django import forms
from .models import Product, Category, MiniCategory
from django.shortcuts import get_object_or_404

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['minicategory', 'name', 'description', 'price', 'image']

