from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

NULLABLE = {"blank":True, "null": True}


class User(AbstractUser):
    user_name = None
    email = models.EmailField(unique= True, verbose_name="email")
    phone = models.CharField(max_length=35,verbose_name="phone number", **NULLABLE)
    telegram = models.CharField(max_length=150,verbose_name="telegram username", **NULLABLE)
    date_birth = models.DateField(verbose_name="date birth")


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_active = models.BooleanField(default=True, verbose_name="activ")

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ['id']