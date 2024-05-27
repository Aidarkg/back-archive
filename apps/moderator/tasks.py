from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task
def send_email_with_credentials(id, password):
    instance = User.objects.get(id=id)
    send_mail(
        subject='Вы были добавлены в модераторы',
        message=f'Ваш логин: {instance.username}\n'
        f'Ваш пароль: {password}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[instance.email],
        fail_silently=False
    )
