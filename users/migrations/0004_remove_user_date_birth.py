# Generated by Django 5.0.13 on 2025-03-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_date_birth'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_birth',
        ),
    ]
