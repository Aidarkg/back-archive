from rest_framework.generics import ListAPIView, RetrieveAPIView

from data_media.models import News
from data_media.serializers.news import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'id'