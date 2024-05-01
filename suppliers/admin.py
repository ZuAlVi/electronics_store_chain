from django.contrib import admin
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Отображение модели Suppliers в админ-панели"""

    list_display = ('id', 'user', 'title', 'levels', 'country', 'city', 'debt', 'created_at')
    list_filter = ('levels', 'title', 'product', 'country',)
    search_fields = ('levels', 'product', 'country')
    actions = ['cleanup_debt']

    def cleanup_debt(self, request, queryset):
        """
        Очистка задолженности
        """
        for supply_object in queryset:
            supply_object.debt = 0
            supply_object.save()
        self.message_user(request, f'Задолженность перед поставщиком у выбранных объектов очищена.')

    cleanup_debt.short_description = 'Очистить задолженность'

