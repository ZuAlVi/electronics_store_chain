from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    """Команда для создания пользователея
     с ролью - user"""

    def handle(self, *args, **options):

        user = User.objects.create(
            email='user@user.ru',
            first_name='user',
            last_name='user',
            role='user',
            is_active=True,
        )
        user.set_password('user')
        user.save()
