from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
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

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
