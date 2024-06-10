from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from user.forms import UserForm
from .models import UserProfile

def logout_view(request):
    logout(request)
    return redirect('market:home')

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
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

    return render(request, 'user/profile.html', {'user_profile': user_profile})