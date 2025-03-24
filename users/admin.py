from django.contrib import admin
from users.models import User
# Register your models here.

# admin.site.register(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("last_name","first_name","pk")
    last_filter = ("last_name",)