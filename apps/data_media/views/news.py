from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from apps.data_media.models import News
from apps.data_media.serializers.news import NewsSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

class NewsListAPIView(ListAPIView):
    queryset = News.objects.all().order_by('-public_date')
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60 * 2))
    def retrieve(self, request, *args, **kwargs):
        return super(NewsListAPIView, self).list(request, *args, **kwargs)


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    @method_decorator(cache_page(60*5))
    def retrieve(self, request, *args, **kwargs):
        return super(NewsDetailAPIView, self).retrieve(request, *args, **kwargs)

