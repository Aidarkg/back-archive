from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from apps.information.serializers.news import NewsSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from ..services.news import NewsService


class NewsListAPIView(ListAPIView):
    queryset = NewsService.get_all_news()
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class NewsDetailAPIView(RetrieveAPIView):
    queryset = NewsService.get_all_news()
    serializer_class = NewsSerializer

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
