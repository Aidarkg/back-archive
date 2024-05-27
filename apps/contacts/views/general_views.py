from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.contacts.models import archive_models
from apps.contacts.models import anticor_cases_models
from apps.contacts.models.coll_center_models import CollCenter
from apps.contacts.serializers import archive_serializers
from apps.contacts.serializers import anticor_cases_serializers
from apps.contacts.serializers import general_serializers


class GeneralListAPIView(APIView):
    def get(self, request):
        general_archive = archive_models.ArchiveContact.objects.all()[:1]
        general_anticor_cases = anticor_cases_models.Anticore.objects.all()[:1]
        coll_center = CollCenter.objects.all()[:1]

        data = {
            'archive': archive_serializers.GeneralSerializer(general_archive, many=True).data,
            'anticor': anticor_cases_serializers.AnticoreSerializer(general_anticor_cases, many=True).data,
            'coll_center': general_serializers.CollCenterSerializer(coll_center, many=True).data,
        }

        return Response(data)
