# market/forms.py

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['minicategory', 'name', 'description', 'price', 'image']