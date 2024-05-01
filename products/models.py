from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Модель продуктов"""

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Хозяин продукта', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название продукта')
    model = models.CharField(max_length=200, verbose_name='Модель продукта')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата релиза продукта')

    def __str__(self):
        return f'{self.title} - {self.model}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
