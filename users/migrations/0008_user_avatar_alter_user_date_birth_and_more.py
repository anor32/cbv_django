# Generated by Django 5.0.13 on 2025-04-01 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_email_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Дата Рождения'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Телеграмм'),
        ),
    ]
