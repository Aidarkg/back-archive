from rest_framework.generics import ListAPIView
from faq.models import Faq
from faq.serializers.faq import FaqSerializer


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
