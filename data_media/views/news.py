from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from data_media.models import News
from data_media.serializers.news import NewsSerializer


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'id'
