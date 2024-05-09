from rest_framework.generics import ListAPIView
from apps.faq.models import Faq
from apps.faq.serializers import FaqSerializer


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
