from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q
from data_media.models import News
from data_media.serializers.news import NewsSerializer


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')

        search_query = self.request.query_params.get('search', None)

        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) | Q(description__icontains=search_query)
            )

        return queryset


class NewsDetailAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_url_kwarg = 'id'