# market/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import Category, MiniCategory, Product
from .forms import ProductForm
from django.http import HttpResponse, JsonResponse

def home(request):
    return render(request, 'market/home.html')

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
    products = Product.objects.filter(available=True)

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

def product_detail(request, name, category_slug, minicategory_slug):
    category = None
    categories = Category.objects.all()
    minicategory = None
    minicategories = MiniCategory.objects.all()
    product = get_object_or_404(Product, name=name, available=True)
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


def product_create(request, category_slug):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('market:product_detail', category_slug=product.category.slug,
                            minicategory_slug=product.minicategory.slug, name=product.name)
    else:
        form = ProductForm()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        minicategories = MiniCategory.objects.filter(category=category)

    return render(request, 'market/product/create.html',
                  {'form': form, 'category': category,
                          'minicategories': minicategories})


def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            # 미니카테고리 필드의 queryset 설정을 위해 clean_category 메서드를 호출
            product.clean_category()
            product.save()
            return redirect('market:product_detail', category_slug=product.category.slug,
                            minicategory_slug=product.minicategory.slug, name=product.slug)
    else:
        form = ProductForm(instance=product)

    return render(request, 'market/product/update.html', {'form': form})

def product_review(request, name):
    product = get_object_or_404(Product, name=name, available=True)

    return render(request, 'market/product/review.html', {'product':product})


def kakaopay_callback(request):
    # 콜백 처리 로직을 여기에 추가
    return HttpResponse('Kakaopay callback handled')