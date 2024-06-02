from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.faq.services.answer_mail import send_answer_mail
from apps.faq.models.question_answer import Question
from apps.faq.tasks import send_mail
from apps.moderator.models import Moderator
from apps.common.utils import get_current_request
from apps.common.middleware import base_url


@receiver(post_save, sender=Question)
def question_pre_save(sender, instance, **kwargs):
    request = get_current_request()
    url = base_url(request)
    moder = Moderator.objects.all()
    email_list = [moderator.email for moderator in moder]
    if instance.is_active:
        send_answer_mail.apply_async(args=(instance.question_text, instance.answer, instance.email))
    if instance.answer is None:
        send_mail.apply_async(args=(instance.id, email_list, url))
