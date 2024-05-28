from celery import shared_task
from django.core.mail import send_mail as sm
from django.template.loader import render_to_string
from apps.faq.models import Question


@shared_task
def send_mail(question_id, **kwargs):
    question = Question.objects.get(id=question_id)
    from_email = kwargs.get('from_email')
    recipient_list = kwargs.get('recipient_list')

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
    })

    sm(
        subject=subject,
        message='',
        html_message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )
