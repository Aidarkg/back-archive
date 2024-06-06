from django.db import models

from apps.common.models.mixins import DateTimeMixin


class Faq(DateTimeMixin):
    question = models.TextField(
        verbose_name='Вопрос'
    )
    answer = models.TextField(
        verbose_name='Ответ'
    )

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос-Ответ'
        verbose_name_plural = 'Вопросы и Ответы'
        ordering = ('-created_at',)
