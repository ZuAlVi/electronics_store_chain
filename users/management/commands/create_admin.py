from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания пользователея
     с ролью - admin"""

    def handle(self, *args, **options):
        # Staff_1
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='admin',
            last_name='admin',
            role='admin',
            is_active=True,
        )
        user.set_password('admin')
        user.save()

