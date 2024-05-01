from django.db import models
from users.models import User
from products.models import Product

from users.models import NULLABLE


class Levels(models.IntegerChoices):
    """Уровни поставщиков"""

    FACTORY = 0, 'Завод'
    RETAIL_NETWORK = 1, 'Розничная сеть'
    ENTREPRENEUR = 2, 'Предприниматель'


class Supplier(models.Model):
    """Модель поставщика"""

    product = models.ManyToManyField(Product, verbose_name='Продукт')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь', **NULLABLE)
    supply = models.ForeignKey('self', on_delete=models.PROTECT, verbose_name='Поставщик', **NULLABLE)

    title = models.CharField(max_length=200, verbose_name='Название')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')
    country = models.CharField(max_length=200, verbose_name='Страна')
    city = models.CharField(max_length=200, verbose_name='Город')
    street = models.CharField(max_length=200, verbose_name='Улица')
    house_number = models.CharField(max_length=100, verbose_name='Номер дома')

    levels = models.IntegerField(choices=Levels.choices, default=Levels.FACTORY, verbose_name='Уровень поставщика')
    debt = models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Задолженность', **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
