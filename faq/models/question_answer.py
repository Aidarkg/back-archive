from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


from faq.validators import validate_phone_number
from moderator.models import Moderator
from django.conf import settings


class Question(models.Model):
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
    topic_question = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Тема вопроса'
    )
    question_text = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Вопрос'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic_question # Надо обсудить


class Answer(models.Model):
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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


@receiver(post_save, sender=Answer)
def send_mail_to_user(sender, instance, **kwargs):
    from faq.tasks import send_mail

    question = instance.question
    answer = instance.answer
    send_mail.delay(
        question.id,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[question.email],
        answer=answer
    )
