import random
import string

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_logged_out, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from users.forms import UserRegisterForm, UserLoginForm, StyleFromMixin, UserUpdateForm, UserPasswordChangeForm
from users.servises import send_new_password, send_register_email


def user_register_view(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            #времено закоментировано проверить через 2 часа
            # send_register_email(new_user.email)
            return HttpResponseRedirect(reverse('users:user_login'))
    context = {
        'title': 'Создать аккаунт',
        'form': UserRegisterForm
    }
    return render(request, 'users/user_register.html', context=context)


def user_login_view(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('dogs:index'))
            return HttpResponse('Вы не пройдете пока не получите бумаги !')



    context = {
        'title': "Вход в аккаунт",
        'form': UserLoginForm
    }
    return render(request, "users/users_login.html", context=context)


@login_required
def user_profile_view(request):
    user_object = request.user
    if user_object.first_name:
        user_name = user_object.first_name
    else:
        user_name = 'Anonymous'

    context = {
        'title': f'Ваш Профиль {user_name} '

    }
    return render(request, 'users/user_profile_read_only.html', context)


@login_required
def user_update_view(request):
    user_object = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, request.FILES , instance=user_object)
        if form.is_valid():
            user_object = form.save()
            user_object.save()
            return HttpResponseRedirect(reverse('users:user_profile'))

    context = {
        'object': user_object,
        "title": f"Изменить профиль {user_object.first_name} {user_object.last_name}",
        'form': UserUpdateForm(instance=user_object)
    }
    return render(request, 'users/user_update.html', context)


def user_logged_out_view(request):
    logout(request)
    return redirect('dogs:index')


@login_required
def user_change_password_view(request):
    user_object = request.user
    form = UserPasswordChangeForm(user_object, request.POST)
    if request.method == "POST":
        if form.is_valid():
            user_object = form.save()
            update_session_auth_hash(request, user_object)
            messages.success(request, "Пароль был Успешно Изменен")
            return HttpResponseRedirect(reverse('users:user_profile'))
        else:
            messages.error(request, "Не удалось изменить пароль")

    context = {
            'form': form
    }
    return render(request, 'users/user_change_password.html', context)


@login_required
def user_generate_new_passport_view(request):
    new_password = ''.join(random.sample((string.ascii_letters+string.digits),12))
    request.user.set_password(new_password)
    request.user.save()
    #времено закоментировано проверить часа через 2
   # send_new_password(request.user.email,new_password)
    return redirect(reverse('dogs:index'))
