from django.urls import path
from apps.data_media.views import VideoDataAPIView, VideoDataRetrieveAPIView, \
    NewsListAPIView, NewsDetailAPIView, \
    PhotoGalleryListAPIView, PhotoGalleryDetailAPIView, \
    ServiceListView, \
    KODEKSListCreateAPIView, KODEKSRetrieveUpdateDestroyAPIView, \
    SearchAPIView, ContactListAPIView, ContactDetailAPIView, \
    VisitorsAPIView, \
    ManagementListAPIView, ManagementDetailAPIView
from apps.data_media.views.organization import OrganizationListView


urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view(), name='video-data-list'),
    path('api/v1/video/<int:pk>', VideoDataRetrieveAPIView.as_view(), name='video-data-detail'),
    path('api/v1/management/', ManagementListAPIView.as_view(), name='management-list'),
    path('api/v1/management/<int:pk>/', ManagementDetailAPIView.as_view(), name='management-detail'),
    path('api/v1/news/', NewsListAPIView.as_view(), name='news-list'),
    path('api/v1/news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('api/v1/photos/', PhotoGalleryListAPIView.as_view(), name='photo-gallery-list'),
    path('api/v1/photos/<int:pk>/', PhotoGalleryDetailAPIView.as_view(), name='photo-gallery-detail'),
    path('api/v1/service/', ServiceListView.as_view(), name='services-list'),
    path('api/v1/kodeks/', KODEKSListCreateAPIView.as_view(), name='kodeks-list'),
    path('api/v1/kodeks/<int:pk>/', KODEKSRetrieveUpdateDestroyAPIView.as_view(), name='kodeks-detail'),
    path('api/v1/contacts', ContactListAPIView.as_view(), name='contacts-list'),
    path('api/v1/contacts/<int:pk>', ContactDetailAPIView.as_view(), name='contacts-detail'),
    path('api/v1/search/', SearchAPIView.as_view(), name='search'),
    path('api/v1/visitors/', VisitorsAPIView.as_view(), name='visitors-list'),
    path('api/v1/organizations/', OrganizationListView.as_view(), name='organizations'),

]
