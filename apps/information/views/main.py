from django.core.exceptions import ObjectDoesNotExist
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contacts.models import Contact
from apps.contacts.serializers.contact_serializers import ContactSerializer
from apps.faq.models.faq import Faq
from apps.faq.serializers.faq import FaqSerializer
from apps.information.models import Logo
from apps.information.models import News, PhotoGallery, VideoData, Organization, Visitors
from apps.information.serializers import LogoSerializer
from apps.information.serializers import NewsSerializer, PhotoListSerializer, VideoDataSerializer, \
    OrganizationSerializer, VisitorSerializer


class MainAPIView(APIView):
    @method_decorator(cache_page(60))
    def get(self, request):
        try:
            visitor, created = Visitors.objects.get_or_create(pk=1)
            visitor.increase_count()

            news = News.objects.all()[:4]
            photogallery = PhotoGallery.objects.all()[:4]
            video_data = VideoData.objects.all()[:4]
            organization = Organization.objects.all()
            faqs = Faq.objects.all()[:5]
            contacts = Contact.objects.first()
            visit = Visitors.objects.all()
            logo = Logo.objects.first()

            data = {
                'logo': LogoSerializer(logo, context={'request': request}).data,
                'news': NewsSerializer(news, many=True, context={'request': request}).data,
                'photo_gallery': PhotoListSerializer(photogallery, many=True, context={'request': request}).data,
                'video_gallery': VideoDataSerializer(video_data, many=True, context={'request': request}).data,
                'organization': OrganizationSerializer(organization, many=True, context={'request': request}).data,
                'faq': FaqSerializer(faqs, many=True).data,
                'contacts': ContactSerializer(contacts).data,
                'visit': VisitorSerializer(visit, many=True).data
            }
            return Response(data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return Response({"detail": "Объект не найден: " + str(e)}, status=status.HTTP_404_NOT_FOUND)
        except APIException as e:
            return Response({"detail": "Ошибка API: " + str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            return Response({"detail": "Произошла непредвиденная ошибка."},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)
