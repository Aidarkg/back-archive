from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

from data_media.models.management import Management
from ..serializers.management import ManagementSerializers


class ManagementListAPIView(ListAPIView):
    serializer_class = ManagementSerializers
    pagination_class = PageNumberPagination


class ManagementDetailAPIView(RetrieveAPIView):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializers
    lookup_url_kwarg = 'id'
