from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from market.models import Category, Product
from user.forms import UserForm
from .models import UserProfile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

def login_success(request):
    username = request.user  # 현재 로그인된 사용자의 이름 가져오기
    return render(request, 'market/home.html', {'username': username})

def logout_view(request):
    logout(request)
    return redirect('market:home')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST, request.FILES) # 파일 업로드 처리 추가
        if form.is_valid():
            user = form.save()
            profile_image = form.cleaned_data.get('profile_image')
            user_profile = UserProfile(user=user, profile_image=profile_image)
            user_profile.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('market:home')
    else:
        form = UserForm()
    return render(request, 'user/signup.html', {'form': form})

def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'user/profile.html', {'user_profile': user_profile})

@login_required
def my_products(request):
    user = request.user
    products = Product.objects.filter(user=user).order_by('-created')

    # 카테고리 필터링
    category_id = request.GET.get('category')
    if category_id:
        category = Category.objects.get(id=category_id)
        products = products.filter(category=category)

    categories = Category.objects.all()

    return render(request, 'user/profile/my_products.html', {
        'products': products,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
    })

class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('market:home')  # 성공 후 리다이렉트할 URL

    def get_object(self, queryset=None):
        return self.request.user
