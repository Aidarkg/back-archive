from apps.faq.tasks import send_mail
from django.conf import settings


class QuestionAnswerService:
    @staticmethod
    def send_question(question) -> None:
        send_mail.delay(
            question.id,
            from_email=question.email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
