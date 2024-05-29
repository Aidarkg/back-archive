from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from ..serializers.management import ManagementListSerializers, ManagementDetailsSerializers
from ..services.management import ManagementService


class ManagementListAPIView(ListAPIView):
    queryset = ManagementService.get_managements()
    serializer_class = ManagementListSerializers
    pagination_class = PageNumberPagination


class ManagementDetailAPIView(RetrieveAPIView):
    queryset = ManagementService.get_managements()
    serializer_class = ManagementDetailsSerializers
