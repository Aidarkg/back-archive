from rest_framework import serializers
from apps.faq.models import Question
from apps.faq.tasks import send_mail
from django.conf import settings


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('full_name', 'email', 'phone_number', 'question_text')

    def save(self, *args, **kwargs):
        question = super(QuestionSerializer, self).save()
        send_mail.delay(
            question.id,
            from_email=question.email,
            recipient_list=[settings.EMAIL_HOST_USER],
        )
