from celery import shared_task
from django.core.mail import send_mail as sm
from django.template.loader import render_to_string
from django.conf import settings
from apps.faq.models import Question
from apps.common.middleware import base_url
from apps.common.utils import get_current_request


@shared_task
def send_mail(instance, recipient_list):
    request = get_current_request()
    url = base_url(request)
    question_id = instance.id

    question = Question.objects.get(id=instance.id)

    subject = 'Архив президента Кыргызской Республики'
    question_text = question.question_text
    full_name = question.full_name
    email = question.email
    phone_number = 'Не указано'
    if question.phone_number:
        phone_number = question.phone_number

    message = render_to_string('question_email.html', {
        'full_name': full_name,
        'email': email,
        'phone_number': phone_number,
        'question': question_text,
        'url': url,
        'id': question_id
    })

    sm(
        subject=subject,
        message='',
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=recipient_list,
        fail_silently=False
    )
