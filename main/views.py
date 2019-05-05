from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, OrderForm, AddMenuForm
from .models import Order, Menu, Restaurant
from django.contrib.auth.models import User


def index(request):
    context = {
        "items": [0, 1, 2]
    }
    return render(request, "main/index.html", context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

# @login_required
# def order(request):
#     if request.method == 'POST':
#         form = OrderForm(request.POST, menus=menus)
#         order = form.save(commit=False)
#         order.menus = menu
#         order.save()
#         # if form.is_valid():
#         #     # Order.objects.create(
#         #     #     user_id=form.cleaned_data.get('user_id'),
#         #     #     menus=form.cleaned_data.get('menu_name'),
#         #     #     description=form.cleaned_data.get('description'),
#         #     #     prepare_time=form.cleaned_data.get('prepare_time'),
#         #     #     image_path=form.cleaned_data.get('image_path'),
#         #     #     price=form.cleaned_data.get('price'),
#         #     #     amount=form.cleaned_data.get('amount'),
#         #     #     status=form.cleaned_data.get('status'),
#         #     # )
#
#             messages.success(request, 'order has been sent!')
#             return redirect('index')
#     else:
#         form = OrderForm()
#     return render(request, 'main/order.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':

        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)

        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'users/profile.html', context)

@login_required
def addMenu(request):
    if request.method == 'POST':
        form = AddMenuForm(request.POST)
        if form.is_valid():
            Menu.objects.create(
                res_id=form.cleaned_data.get('res_id'),
                menu_name=form.cleaned_data.get('menu_name'),
                description=form.cleaned_data.get('description'),
                prepare_time=form.cleaned_data.get('prepare_time'),
                image_path=form.cleaned_data.get('image_path'),
                price=form.cleaned_data.get('price'),
                amount=form.cleaned_data.get('amount'),
                status=form.cleaned_data.get('status'),
            )
            messages.success(request, 'order has been sent!')
            return redirect('addMenu')
    else:
        form = AddMenuForm()
    return render(request, 'main/addMenu.html', {'form': form})