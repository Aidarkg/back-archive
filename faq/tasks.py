from celery import shared_task
from django.core.mail import send_mail as sm

from faq.models import Question


@shared_task
def send_mail(question_id, **kwargs):
    question = Question.objects.get(id=question_id)
    from_email = kwargs.get('from_email')
    recipient_list = kwargs.get('recipient_list')

    answer = kwargs.get('answer', None)
    if answer is not None:
        message = f' {answer}'
    else:
        message = f'{question.question_text}'

    sm(
        f'Тема вопроса: {question.topic_question}',
        message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )
