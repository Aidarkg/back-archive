from rest_framework.views import APIView
from rest_framework.response import Response
from .models import News, KODEKS, PhotoGallery, VideoData, Service, Management
from .serializers import NewsSerializer,  PhotoGallerySerializer, VideoDataSerializer, ServiceSerializers
from django.db.models import Q

from .serializers.kodeks import KODEKSSerializer
from .serializers.management_serializers import ManagementSerializers


class SearchAPIView(APIView):
    def get(self, request, *args, **kwargs):
        query = request.query_params.get('query', None)
        if query is not None:
            news = News.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
            codexes = KODEKS.objects.filter(title__icontains=query)
            photos = PhotoGallery.objects.filter(description__icontains=query)
            videos = VideoData.objects.filter(description__icontains=query)
            services = Service.objects.filter(name__icontains=query)
            managementes = Management.objects.filter(name__icontains=query)

            results = {
                'news': NewsSerializer(news, many=True).data,
                'codexes': KODEKSSerializer(codexes, many=True).data,
                'photos': PhotoGallerySerializer(photos, many=True).data,
                'videos': VideoDataSerializer(videos, many=True).data,
                'services': ServiceSerializers(services, many=True).data,
                'managementes': ManagementSerializers(managementes, many=True).data

            }

            return Response(results)
        return Response({"message": "Поисковый запрос не предоставлен"}, status=400)
