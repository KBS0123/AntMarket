from django.shortcuts import render, get_object_or_404
from .models import Category, MiniCategory, Product

def home(request):
    return render(request, 'market/home.html')

def product_list(request, category_slug=None, minicategory_slug=None):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        if minicategory_slug:
            category = get_object_or_404(Category, slug=category_slug)
            minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)
            products =products.filter(minicategory=minicategory)

    return render(request, 'market/product/list.html',
                  {
                      'category': category, 'categories': categories,
                      'minicategory': minicategory, 'minicategories': minicategories,
                      'products': products
                  })

def product_detail(request, slug, category_slug, minicategory_slug):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()

    if category_slug:
        if minicategory_slug:
            category = get_object_or_404(Category, slug=category_slug)
            minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)
            product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'market/product/detail.html',
                  {
                      'category': category, 'categories': categories,
                      'minicategory': minicategory, 'minicategories': minicategories,
                      'product': product
                  })