from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # Поля, которые будут видны в списке студентов
    list_display = ('fio', 'phone', 'email', 'join_date', 'is_active', 'created_at')

    # Поля, по которым можно кликнуть, чтобы перейти к редактированию
    list_display_links = ('fio',)

    # Боковой фильтр для быстрой сортировки
    list_filter = ('is_active', 'join_date', 'created_at')

    # Поля для поиска (по ФИО, почте или телефону)
    search_fields = ('fio', 'email', 'phone')

    # Возможность редактировать активность прямо из списка
    list_editable = ('is_active',)

    # Группировка полей при редактировании записи
    fieldsets = (
        ('Личные данные', {
            'fields': ('fio', 'date_of_birth', 'email', 'phone')
        }),
        ('Статус обучения', {
            'fields': ('join_date', 'is_active')
        }),
        ('Системная информация', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Скрывает блок по умолчанию
        }),
    )

    # Эти поля нельзя редактировать вручную, так как они auto_now
    readonly_fields = ('created_at', 'updated_at')