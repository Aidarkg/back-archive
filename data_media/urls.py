from django.urls import path

from data_media.views import VideoDataAPIView, VideoDataRetriveAPIView, \
                             NewsListAPIView, NewsDetailAPIView, \
                             PhotoGalleryListAPIView, PhotoGalleryDetailAPIView, \
                             ServiceListView, ServiceDetailView
from data_media.views.management_views import ManagementListAPIView, ManagementDetailAPIView


urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view()),
    path('api/v1/video/<int:id>', VideoDataRetriveAPIView.as_view()),
    path('api/v1/management/', ManagementListAPIView.as_view()),
    path('api/v1/management/<int:pk>/', ManagementDetailAPIView.as_view()),
    path('api/v1/news/', NewsListAPIView.as_view()),
    path('api/v1/news/<int:id>/', NewsDetailAPIView.as_view()),
    path('api/v1/photos/', PhotoGalleryListAPIView.as_view()),
    path('api/v1/photos/<int:pk>/', PhotoGalleryDetailAPIView.as_view()),
    path('api/v1/service/', ServiceListView.as_view()),
    path('api/v1/service/<int:pk>/', ServiceDetailView.as_view()),
]
