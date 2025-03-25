# Generated by Django 5.0.13 on 2025-03-25 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='dog_breed')),
            ],
            options={
                'verbose_name': 'breed',
                'verbose_name_plural': 'breeds',
            },
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='dog_name')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='dogs/', verbose_name='image')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth_date')),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dogs.breed', verbose_name='breed')),
            ],
            options={
                'verbose_name': 'dog',
                'verbose_name_plural': 'dogs',
                'db_table': 'our_dogs',
            },
        ),
    ]
