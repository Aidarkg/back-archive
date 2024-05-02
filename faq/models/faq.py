from django.db import models


class Faq(models.Model):
    question = models.CharField(
        max_length=500,
        null=False,
        blank=False,
        verbose_name='Вопрос'
    )
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
