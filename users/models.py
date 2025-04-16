from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {"blank": True, "null": True}


class UserRoles(models.TextChoices):
    ADMIN = 'admin', _('admin')
    MODERATOR = 'moderator', _('moderator')
    USER = 'user', _('user')


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, default=None, verbose_name="username", **NULLABLE)
    role = models.CharField(max_length=9, choices=UserRoles.choices, default=UserRoles.USER)
    email = models.EmailField(unique=True, verbose_name="Эл. почта")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE)
    first_name = models.CharField(max_length=150, verbose_name="имя", default="Anonymous")
    last_name = models.CharField(max_length=150, verbose_name="фамилия", default="Anonymous")
    telegram = models.CharField(max_length=150, verbose_name="Телеграмм", **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name="Аватар", **NULLABLE)
    date_birth = models.DateField(verbose_name="Дата Рождения", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="activ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['id']
