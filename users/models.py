from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    """
    Кастомный пользователь: логин по email, доп. поля: phone, city, avatar.
    Поле username удаляем.
    """
    username = None  # отключаем username
    email = models.EmailField("Email", unique=True)

    phone = models.CharField("Телефон", max_length=32, blank=True)
    city = models.CharField("Город", max_length=120, blank=True)
    avatar = models.ImageField("Аватар", upload_to="avatars/", blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # при createsuperuser запросит только email и пароль

    objects = UserManager()

    def __str__(self):
        return self.email