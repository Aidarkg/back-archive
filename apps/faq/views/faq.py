from rest_framework.generics import ListAPIView
from apps.faq.serializers import FaqSerializer
from apps.faq.models import Faq


class FaqListAPIView(ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer
