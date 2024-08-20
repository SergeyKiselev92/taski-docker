"""Файл с сериализатором приложения."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для преобразования в Python-объекты модели Taski."""

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'completed')
