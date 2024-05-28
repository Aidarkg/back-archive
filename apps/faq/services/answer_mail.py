from django.conf import settings
from celery import shared_task
from django.template.loader import render_to_string
from django.core.mail import send_mail as sm


@shared_task
def send_answer_mail(question, answer, email):
    subject = 'Архив президента Кыргызской Республики'
    message = render_to_string('answer_email.html', {
        'question': question,
        'answer': answer,
    })
    sm(
        subject=subject,
        message='',
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
    )
