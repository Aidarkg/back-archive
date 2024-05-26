from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Q
from apps.data_media.models import PhotoGallery, KODEKS, News, VideoData, Service, Management
from apps.data_media.serializers import (
    NewsSerializer, KODEKSSerializer, PhotoGallerySerializer, VideoDataSerializer,
    ServiceSerializers, ManagementListSerializers
)

class CustomPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 100


class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('search', None)
        if query is not None:
            paginator = CustomPagination()
            results = {}

            def paginate_queryset(queryset, serializer_class, category):
                paginated_queryset = paginator.paginate_queryset(queryset, request)
                serialized_data = serializer_class(paginated_queryset, many=True).data
                results.update({
                    f'{category}_count': paginator.count,
                    f'{category}_next': paginator.get_next_link(),
                    f'{category}_previous': paginator.get_previous_link(),
                    f'{category}_results': serialized_data
                })

            categories = {
                'news': (News.objects.filter(title__icontains=query), NewsSerializer),
                'codexes': (KODEKS.objects.filter(title__icontains=query), KODEKSSerializer),
                'photos': (PhotoGallery.objects.filter(title__icontains=query), PhotoGallerySerializer),
                'videos': (VideoData.objects.filter(title__icontains=query), VideoDataSerializer),
                'services': (Service.objects.filter(title__icontains=query), ServiceSerializers),
                'managements': (Management.objects.filter(full_name__icontains=query), ManagementListSerializers)
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
