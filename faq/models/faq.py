from django.db import models

from common.models.mixins import DateTimeMixin


class Faq(DateTimeMixin):
    question = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Вопрос'
    )
    answer = models.TextField()

    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы и Ответы'
