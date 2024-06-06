from django.urls import path
from apps.faq.views import faq


urlpatterns = [
    path('faq/', faq.FaqListAPIView.as_view(), name='faq-list'),
]
