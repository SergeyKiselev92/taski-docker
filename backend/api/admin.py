"""Файл для отображения модели в панели администратора."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Настройка панели администратора."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
