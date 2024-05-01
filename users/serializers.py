from djoser.serializers import UserCreateSerializer

from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserRegistrationSerializer(UserCreateSerializer):
    """
    Сериализатор модели User.
    Регистрация пользователя.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']


class CurrentUserSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели User.
    Отображение данных пользователя.
    """
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password']
