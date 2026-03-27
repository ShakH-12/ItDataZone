from django.contrib import admin
from .models import Teammate, Role


@admin.register(Teammate)
class TeammateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'is_active')
    search_fields = ('full_name', 'role',)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)