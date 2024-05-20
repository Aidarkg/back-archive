from django.urls import path
from apps.faq.views import faq
from apps.faq.views.question_answer import question_create_view


urlpatterns = [
    path('api/v1/faq/', faq.FaqListAPIView.as_view(), name='faq-list'),
    path('api/v1/question/create/', question_create_view, name='question-create'),
]
