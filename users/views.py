from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_logged_out, update_session_auth_hash
from django.contrib.auth.decorators import login_required

from django.contrib import messages
from users.forms import UserRegisterForm, UserLoginForm, StyleFromMixin, UserUpdateForm, UserPasswordChangeForm


def user_register_view(request):
    form = UserRegisterForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            new_user = form.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users/users_login'))
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
                else:
                    return HttpResponse('Аккаунт Неактивен!')
            else:
                print("Неверное имя пользователя или пароль")

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
