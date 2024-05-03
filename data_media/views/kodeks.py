from rest_framework import generics
from data_media.models.kodeks import KODEKS
from data_media.serializers.kodeks import KODEKSSerializer
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q


class KODEKSListCreateAPIView(generics.ListAPIView):
    serializer_class = KODEKSSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = KODEKS.objects.all().order_by('-created_at')

        search_query = self.request.query_params.get('search', None)
        
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query)
            )
        
        return queryset


class KODEKSRetrieveUpdateDestroyAPIView(generics.RetrieveAPIView):
    queryset = KODEKS.objects.all()
    serializer_class = KODEKSSerializer
    lookup_url_kwarg = 'id'
