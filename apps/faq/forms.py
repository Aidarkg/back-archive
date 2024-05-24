import pdb

from django import forms
from apps.faq.models import Answer
from django.conf import settings


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            'moderator',
            'question',
            'answer'
        )

    def save(self, *args, **kwargs):
        instance = super(AnswerForm, self).save(*args, **kwargs)
        from apps.faq.tasks import send_mail

        question = instance.question
        answer = instance.answer
        send_mail.delay(
            question.id,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[question.email],
            answer=answer
        )
        return instance