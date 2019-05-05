from django import forms
from .models import User, Order
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'image_path']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'image_path']


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['user_id', 'menus', 'receive_datetime', 'comment']

