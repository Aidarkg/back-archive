from django.urls import path
from apps.faq.views import faq


urlpatterns = [
    path('api/v1/faq/', faq.FaqListAPIView.as_view(), name='faq-list'),
]
