import random
import string

from django.shortcuts import render, reverse, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout, user_logged_out, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.views import LoginView, PasswordChangeView, LogoutView
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from users.models import User
from users.forms import UserRegisterForm, UserLoginForm, StyleFromMixin, UserUpdateForm, UserPasswordChangeForm, \
    UserForm
from users.servises import send_new_password, send_register_email


class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('dogs:index')
    template_name = 'users/user_register.html'
    extra_context = {
            'title': 'Создать аккаунт',
        }




class UserLoginView(LoginView):
    template_name = 'users/user_login.html'
    form_class = UserLoginForm
    extra_context = {
        'title': 'Вход В аккаунт',
    }




class UserProfileView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/user_profile_read_only.html'
    extra_context = {
        'title': f'Ваш Профиль '
    }

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title': 'Обновить профиль',
    }

    def get_object(self, queryset=None):
        return self.request.user





class UserLogoutView(LogoutView):
    template_name = 'users/user_logout.html'
    extra_context = {
        'title': 'Выход из аккаунта',
    }
class UserChangePasswordView(PasswordChangeView):
    from_class = UserPasswordChangeForm
    template_name = 'users/user_change_password.html'
    success_url = reverse_lazy('users:user_profile')
    extra_context = {
        'title': 'Измениние пароля',
    }


def user_generate_new_passport_view(request):
    new_password = ''.join(random.sample((string.ascii_letters + string.digits), 12))
    request.user.set_password(new_password)
    request.user.save()
    # времено закоментировано проверить часа через 2
    # send_new_password(request.user.email,new_password)
    return redirect(reverse('dogs:index'))
