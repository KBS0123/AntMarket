# market/views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, MiniCategory, Product
from .forms import ProductForm

def home(request):
    return render(request, 'market/home.html')

def product_list(request, category_slug=None, minicategory_slug=None):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)

        if minicategory_slug:
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
    product = get_object_or_404(Product, slug=slug, available=True)

    if category_slug and minicategory_slug:
        category = get_object_or_404(Category, slug=category_slug)
        minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)

    return render(request, 'market/product/detail.html',
                  {
                      'category': category, 'categories': categories,
                      'minicategory': minicategory, 'minicategories': minicategories,
                      'product': product
                  })

def product_update(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('market:home')  # 등록 후 홈 페이지로 이동
    else:
        form = ProductForm()
    return render(request, 'market/product/update.html', {'form': form})
