from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

NULLABLE = {"blank":True, "null": True}


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=False, default=None, verbose_name="username", **NULLABLE)
    email = models.EmailField(unique= True, verbose_name="Эл. почта")
    phone = models.CharField(max_length=35,verbose_name="Телефон", **NULLABLE)
    first_name = models.CharField(max_length=150, verbose_name="имя", default = "Anonymous")
    last_name = models.CharField(max_length=150, verbose_name="фамилия")
    telegram = models.CharField(max_length=150,verbose_name="telegram username", **NULLABLE)
    date_birth = models.DateField(verbose_name="date birth", **NULLABLE)
    is_active = models.BooleanField(default=True, verbose_name="activ")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['id']