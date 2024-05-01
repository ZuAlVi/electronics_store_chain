from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    """
    Пользователи - отображение в админ-панели Jango.
    Фильтрует по роли пользователя.
    """

    list_display = ('id', 'email', 'first_name', 'last_name', 'role', 'is_active')
    list_filter = ('role',)
