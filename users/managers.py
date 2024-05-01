from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """ Класс создания пользователя"""

    def create_user(self, email, first_name, last_name, password, role='user'):
        """Функция создания пользователя
         — в нее мы передаем обязательные поля"""
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            role=role,
        )

        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, password, role='admin'):
        """
        Функция для создания суперпользователя
        — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
            role=role
        )

        user.is_active = True

        user.save(using=self._db)

        return user
