from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('fio', 'phone', 'email')
    list_filter = ('fio', 'phone', 'email')
    search_fields = ('id', 'fio', 'phone', 'email')