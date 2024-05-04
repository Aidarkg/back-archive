from django.db import models
from common.models.mixins import DateTimeMixin
from faq.validators import validate_phone_number
from moderator.models import Moderator


class Question(DateTimeMixin):
    full_name = models.CharField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='полное имя'
    )
    email = models.EmailField(
        max_length=150,
        null=False,
        blank=False,
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False,
        verbose_name='Номер телефона',
        validators=[validate_phone_number]
    )
    question_text = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Вопрос'
    )

    def __str__(self):
        return self.question_text


class Answer(DateTimeMixin):
    moderator = models.ForeignKey(
        Moderator,
        on_delete=models.DO_NOTHING,
        related_name='moderator_answer'
    )
    question = models.ForeignKey(
        Question,
        on_delete=models.DO_NOTHING,
        related_name='question_answer'
    )
    answer = models.TextField()
