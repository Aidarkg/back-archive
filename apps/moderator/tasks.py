from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from celery import shared_task


@shared_task
def send_email_with_credentials(username, password, email):
    subject = 'Архив президента Кыргызской Республики'
    message = render_to_string('register_moder.html', {
        'login': username,
        'password': password
    })

    send_mail(
        subject=subject,
        message='',
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
