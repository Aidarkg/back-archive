from rest_framework import serializers
from apps.faq.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('full_name', 'email', 'phone_number', 'question_text')
