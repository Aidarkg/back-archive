from rest_framework.generics import ListAPIView
from apps.faq.serializers import FaqSerializer
from ..services.faq import FaqService


class FaqListAPIView(ListAPIView):
    queryset = FaqService.get_faqs()
    serializer_class = FaqSerializer
