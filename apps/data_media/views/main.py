from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import APIException
from rest_framework import status

from apps.data_media.models import News, PhotoGallery, VideoData, Organization, Contact, Visit
from apps.faq.models.faq import Faq

from apps.data_media.serializers import NewsSerializer, PhotoListSerializer, VideoDataSerializer, \
    OrganizationSerializer, ContactSerializer, VisitSerializer, PhotoGallerySerializer
from apps.faq.serializers.faq import FaqSerializer


class MainAPIView(APIView):
    def get(self, request):
        try:
            news = News.objects.all()[:4]
            photogallery = PhotoGallery.objects.all()[:4]
            video_data = VideoData.objects.all()[:4]
            organization = Organization.objects.all()
            contact = Contact.objects.all()
            faqs = Faq.objects.all()
            visit = Visit.objects.all()

            data = {
                'news': NewsSerializer(news, many=True, context={'request': request}).data,
                'photo_gallery': PhotoListSerializer(photogallery, many=True, context={'request': request}).data,
                'video_gallery': VideoDataSerializer(video_data, many=True, context={'request': request}).data,
                'organization': OrganizationSerializer(organization, many=True, context={'request': request}).data,
                'contact': ContactSerializer(contact, many=True).data,
                'faq': FaqSerializer(faqs, many=True).data,
                'visit': VisitSerializer(visit, many=True).data,
            }
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({"detail": "Объект не найден: " + str(e)}, status=status.HTTP_404_NOT_FOUND)
        except APIException as e:
            return Response({"detail": "Ошибка API: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"detail": "Произошла непредвиденная ошибка."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
