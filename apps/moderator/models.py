from django.db import models
from django.contrib.auth.models import User, Group
from .moderator_services import save_moderator, generate_password
from apps.common.models.mixins import DateTimeMixin


class Moderator(DateTimeMixin):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name="Имя пользователя"
    )
    email = models.EmailField(
        unique=True,
        verbose_name="Электронная почта",
    )
    password = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Пароль',
        help_text='Пароль будет генерирован автоматически'
    )
    group = models.ForeignKey(
        'CustomGroup',
        on_delete=models.CASCADE,
        verbose_name='Группа'
    )

    class Meta:
        verbose_name = 'Модератор'
        verbose_name_plural = 'Модераторы'

    def save(self, *args, **kwargs):
        if self.pk is None:
            password = generate_password()
            self.password = password
        super().save(*args, **kwargs)
        save_moderator(self, *args, **kwargs)

    def __str__(self):
        return self.username


class CustomGroup(Group):
    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
