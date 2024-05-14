# from django.conf import settings
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from apps.faq.models import Answer
#
#
# @receiver(post_save, sender=Answer)
# def send_mail_to_user(sender, instance, **kwargs):
#     from apps.faq.tasks import send_mail
#
#     question = instance.question
#     answer = instance.answer
#     send_mail.delay(
#         question.id,
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[question.email],
#         answer=answer
#     )
