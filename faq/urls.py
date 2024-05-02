from django.urls import path
from faq.views import faq_view
from faq.views.question_answer_view import question_create_view


urlpatterns = [
    path('api/v1/faq/', faq_view.FaqAPIView.as_view()),
    path('api/v1/faq/<int:pk>/', faq_view.FaqAPIDetailPIView.as_view()),
    path('api/v1/question/create/', question_create_view),
]
