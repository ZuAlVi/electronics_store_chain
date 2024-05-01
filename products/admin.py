from django.contrib import admin
from products.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Отображает модель Product в админ-панели
    Фильтрует по хозяину продукта и названию продукта.
    Поиск по названию продукта.
    """
    list_display = ('id', 'user', 'title', 'model', 'release_date')
    list_filter = ('user', 'title',)
    search_fields = ('title',)

