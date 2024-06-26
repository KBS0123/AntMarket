from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class UserForm(UserCreationForm):
    email = forms.EmailField(label="이메일")
    profile_image = forms.ImageField(label="프로필 이미지", required=False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2", "email", "profile_image")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image']