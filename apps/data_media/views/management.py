from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from apps.data_media.models.management import Management
from ..serializers.management import ManagementSerializers


class ManagementListAPIView(ListAPIView):
    queryset = Management.objects.all().order_by('-created_at')
    serializer_class = ManagementSerializers
    pagination_class = PageNumberPagination


class ManagementDetailAPIView(RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializers
