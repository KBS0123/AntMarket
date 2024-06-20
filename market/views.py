# market/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q

from cart.cart import Cart
from cart.forms import CartAddProductForm
from .models import Category, MiniCategory, Product
from .forms import ProductForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST

def home(request):
    products = Product.objects.order_by('?')

    return render(request, 'market/home.html',
                  {'products':products})

def search(request):
    kw = request.GET.get('kw', '')  # 검색어
    products = Product.objects.order_by('-created')

    if kw:
        products = products.filter(
            Q(name__icontains=kw) |  # 제목 검색
            Q(description__icontains=kw)  # 내용 검색
        ).distinct()

    return render(request, 'market/product/search.html', {'kw':kw, 'products':products})

def product_list(request, category_slug=None, minicategory_slug=None):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()
    products = Product.objects.filter(available=True).order_by('-created')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        minicategories = MiniCategory.objects.filter(category=category)
        products = products.filter(category=category)

        if minicategory_slug:
            minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)
            products =products.filter(minicategory=minicategory)

    return render(request, 'market/product/product_list.html',
                  {
                      'category': category, 'categories': categories,
                      'minicategory': minicategory, 'minicategories': minicategories,
                      'products': products
                  })

def product_detail(request, id, category_slug, minicategory_slug):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()

    if category_slug and minicategory_slug:
        category = get_object_or_404(Category, slug=category_slug)
        minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)

    return render(request, 'market/product/detail.html',
                  {
                      'category': category, 'categories': categories,
                      'minicategory': minicategory, 'minicategories': minicategories,
                      'product': product, 'cart_product_form': cart_product_form
                  })

@login_required
def product_create(request, category_slug):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        minicategories = MiniCategory.objects.filter(category=category)

        if request.method == 'POST':
            form = ProductForm(request.POST, request.FILES)
            if form.is_valid():
                product = form.save(commit=False)
                product.user = request.user
                product.category = category
                product.save()
                return redirect('market:product_detail', category_slug=product.category.slug,
                                minicategory_slug=product.minicategory.slug, id=product.id)
        else:
            form = ProductForm()

    return render(request, 'market/product/create.html',
                  {'form': form, 'category': category,
                          'minicategories': minicategories})

@login_required
def product_update(request, category_slug, minicategory_slug, id):
    product = get_object_or_404(Product, category__slug=category_slug, minicategory__slug=minicategory_slug, id=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('market:product_detail', category_slug=product.category.slug,
                            minicategory_slug=product.minicategory.slug, id=product.id)
    else:
        form = ProductForm(instance=product)

    category = product.category
    minicategories = MiniCategory.objects.filter(category=category)
    minicategory = product.minicategory

    return render(request, 'market/product/update.html',
                  {'form': form, 'category': category, 'product': product,
                   'minicategories': minicategories, 'minicategory': minicategory})

@login_required
@require_POST
def product_delete(request, category_slug, minicategory_slug, id):
    product = get_object_or_404(Product, category__slug=category_slug, minicategory__slug=minicategory_slug, id=id)
    cart = Cart(request)
    cart.remove_product_by_id(product.id)
    product.delete()
    return JsonResponse({'message': 'Product deleted successfully'}, status=200)
