from django.conf import settings
from django.db import models

from users.models import NULLABLE


class Breed(models.Model):
    name = models.CharField(max_length=100, verbose_name='dog_breed')
    description = models.CharField(max_length=1000,verbose_name="description", **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'breed'
        verbose_name_plural = 'breeds'


class Dog(models.Model):
    name = models.CharField(max_length=250, verbose_name='Кличка')
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name="Порода")
    photo = models.ImageField(upload_to='dogs/', **NULLABLE, verbose_name="Фото")
    birth_date = models.DateField(**NULLABLE, verbose_name="Дата Рождения")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name="Хозяин")

    def __str__(self):
        return f'{self.name} ({self.breed})'

    class Meta:
        verbose_name = 'dog'
        verbose_name_plural = "dogs"
        db_table = 'our_dogs'


class DogParent(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    name  = models.CharField(max_length=150, verbose_name='Кличка Родителя')
    category = models.ForeignKey(Breed, on_delete=models.CASCADE, verbose_name='Порода Родителя')
    birth_date = models.DateField(**NULLABLE,verbose_name=' Дата Рождения Родителя')

    def __str__(self):
        return f'{self.name} ({self.breed})'

    class Meta:
        verbose_name = 'parrent'
        verbose_name_plural = 'parrents'