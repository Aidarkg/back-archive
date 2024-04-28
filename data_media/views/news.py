from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from data_media.models import News
from data_media.serializers.news import NewsSerializer


class NewsListAPIView(ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination
    filterset_fields = ['title', 'description']


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'id'