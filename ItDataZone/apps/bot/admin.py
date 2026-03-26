from django.contrib import admin
from .models import User, RegisteredUser


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'is_active',)
    list_filter = ('created_at', 'is_active',)
    search_fields = ('id',)
    ordering = ('-created_at',)


@admin.register(RegisteredUser)
class RegisteredUserAdmin(admin.ModelAdmin):
    list_display = ("user", "full_name", "course",)