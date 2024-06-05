from django.db import models
from apps.common.models.mixins import DateTimeMixin
from apps.moderator.models import Moderator


class Question(DateTimeMixin):
    full_name = models.CharField(
        max_length=150,
        verbose_name='Полное имя'
    )
    email = models.EmailField(
        max_length=150,
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='Номер телефона',
    )
    question_text = models.TextField(
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        null=True,
        blank=True,
        verbose_name='Ответ'
    )
    moderator = models.ForeignKey(
        Moderator,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='questions',
        verbose_name='Модератор'
    )
    is_active = models.BooleanField(default=False, verbose_name='Отправить сообщение?')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Вопрос пользователя'
        verbose_name_plural = 'Вопросы пользователя'
