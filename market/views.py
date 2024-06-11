# market/views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from cart.forms import CartAddProductForm
from .models import Category, MiniCategory, Product
from .forms import ProductForm

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

        if minicategory_slug:
            minicategory = get_object_or_404(MiniCategory, slug=minicategory_slug)
            products =products.filter(minicategory=minicategory)

    return render(request, 'market/product/list.html',
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


@login_required
def product_update(request):
    selected_category_id = request.POST.get('category')
    selected_category = None
    minicategories = []

    if selected_category_id:
        selected_category = get_object_or_404(Category, id=selected_category_id)
        minicategories = selected_category.minicategory_set.all()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('market:home')  # 등록 후 홈 페이지로 이동
    else:
        form = ProductForm()

    # 카테고리 목록을 템플릿으로 전달
    categories = Category.objects.all()

    return render(request, 'market/product/update.html',
                  {'form': form, 'categories': categories, 'selected_category': selected_category, 'minicategories': minicategories})

def product_review(request, name):
    product = get_object_or_404(Product, name=name, available=True)

    return render(request, 'market/product/review.html', {'product':product})
