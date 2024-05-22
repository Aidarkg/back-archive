import re
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from apps.faq.models import Question


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('full_name', 'email', 'phone_number', 'question_text')

    def validate_phone_number(self, value):
        pattern = r'^\+996\d{9}$'
        if not re.match(pattern, value):
            raise ValidationError('Номер телефона должен быть в действующем международном формате.')
        return value
