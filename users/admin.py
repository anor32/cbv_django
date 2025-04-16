from django.contrib import admin
from users.models import User
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("pk","email","last_name","first_name","role","is_active")
    last_filter = ("last_name",)