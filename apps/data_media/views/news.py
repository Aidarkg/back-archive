from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from apps.data_media.models import News
from apps.data_media.serializers.news import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-public_date')
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
