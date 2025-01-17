from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from celery import shared_task
from apps.moderator.models import Moderator
from apps.common.utils import get_current_request
from apps.common.middleware import base_url


@shared_task
def send_email_with_credentials(username, password, email, url):
    subject = 'Архив президента Кыргызской Республики'
    message = render_to_string('register_moder.html', {
        'login': username,
        'password': password,
        'url': url
    })

    send_mail(
        subject=subject,
        message='',
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )


@receiver(post_save, sender=Moderator)
def data_mail_save(sender, instance, created, **kwargs):
    request = get_current_request()
    url = base_url(request)
    if created:
        send_email_with_credentials.delay(instance.username, instance.password, instance.email, url)


@receiver(post_delete, sender=Moderator)
def delete_user(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except Exception as e:
        pass
