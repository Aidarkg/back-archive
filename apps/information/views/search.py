from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from apps.information.models import PhotoGallery, KODEKS, News, VideoData, Service, Management
from apps.information.serializers import (
    NewsSerializer, KODEKSSerializer, PhotoListSerializer, VideoDataSerializer,
    ServiceSerializers, ManagementListSerializers
)


class CustomPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class SearchAPIView(APIView):
    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('search', '')
        if query:
            paginator = CustomPagination()
            results = {}
            search_filters = Q(title__icontains=query)

            def paginate_queryset(queryset, serializer_class, category):
                paginated_queryset = paginator.paginate_queryset(queryset, request, view=self)
                serialized_data = serializer_class(paginated_queryset, many=True, context={'request': request}).data
                results.update({
                    f'{category}_count': paginator.count,
                    f'{category}_next': paginator.get_next_link(),
                    f'{category}_previous': paginator.get_previous_link(),
                    f'{category}_results': serialized_data
                })

            categories = {
                'news': (News.objects.filter(search_filters), NewsSerializer),
                'codexes': (KODEKS.objects.filter(search_filters), KODEKSSerializer),
                'photos': (PhotoGallery.objects.filter(search_filters), PhotoListSerializer),
                'videos': (VideoData.objects.filter(search_filters), VideoDataSerializer),
                'services': (Service.objects.filter(search_filters), ServiceSerializers),
                'managements': (Management.objects.filter(Q(full_name__icontains=query)), ManagementListSerializers)
            }

            for category, (queryset, serializer_class) in categories.items():
                if queryset.exists():
                    paginate_queryset(queryset, serializer_class, category)
                else:
                    results[f'{category}_count'] = 0
                    results[f'{category}_next'] = None
                    results[f'{category}_previous'] = None
                    results[f'{category}_results'] = []

            return Response(results)

        return Response({"message": "Поисковый запрос не предоставлен"}, status=400)
