from django.urls import path
from faq.views import faq
from faq.views.question_answer import question_create_view


urlpatterns = [
    path('api/v1/faq/', faq.FaqListAPIView.as_view()),
    path('api/v1/question/create/', question_create_view),
]
