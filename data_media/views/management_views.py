from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from data_media.models.management import Management
from ..serializers.management_serializers import ManagementSerializers


class ManagementListAPIView(ListAPIView):
    serializer_class = ManagementSerializers
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Management.objects.all().order_by('-created_at')

        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query)
            )
        return queryset
    

class ManagementDetailAPIView(RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializers
    lookup_url_kwarg = 'id'
