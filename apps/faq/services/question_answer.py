from apps.faq.tasks import send_mail
from django.conf import settings

from apps.moderator.models import Moderator


class QuestionAnswerService:
    @staticmethod
    def send_question(question) -> None:
        moder = Moderator.objects.all()
        email_list = [moderator.email for moderator in moder]
        if email_list:
            send_mail.delay(
                question.id,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=email_list,
            )
