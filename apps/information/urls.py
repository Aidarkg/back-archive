from django.urls import path
from apps.information.views import VideoDataAPIView, \
    NewsListAPIView, NewsDetailAPIView, \
    PhotoGalleryListAPIView, PhotoGalleryDetailAPIView, \
    ServiceListView, \
    KODEKSListCreateAPIView, KODEKSRetrieveUpdateDestroyAPIView, \
    SearchAPIView, \
    VisitorsAPIView, \
    ManagementListAPIView, ManagementDetailAPIView, \
    MainAPIView, VideoLinkAPIView
from apps.information.views.organization import OrganizationListView


urlpatterns = [
    path('api/v1/video/', VideoDataAPIView.as_view(), name='video-data-list'),
    path('api/v1/video_link/', VideoLinkAPIView.as_view(), name='video-link-data-list'),
    path('api/v1/management/', ManagementListAPIView.as_view(), name='management-list'),
    path('api/v1/management/<int:pk>/', ManagementDetailAPIView.as_view(), name='management-detail'),
    path('api/v1/news/', NewsListAPIView.as_view(), name='news-list'),
    path('api/v1/news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('api/v1/photos/', PhotoGalleryListAPIView.as_view(), name='photo-gallery-list'),
    path('api/v1/photos/<int:pk>/', PhotoGalleryDetailAPIView.as_view(), name='photo-gallery-detail'),
    path('api/v1/service/', ServiceListView.as_view(), name='services-list'),
    path('api/v1/kodeks/', KODEKSListCreateAPIView.as_view(), name='kodeks-list'),
    path('api/v1/kodeks/<int:pk>/', KODEKSRetrieveUpdateDestroyAPIView.as_view(), name='kodeks-detail'),
    path('api/v1/search/', SearchAPIView.as_view(), name='search'),
    path('api/v1/visitors/', VisitorsAPIView.as_view(), name='visitors-list'),
    path('api/v1/organizations/', OrganizationListView.as_view(), name='organizations'),
    path('api/v1/main/', MainAPIView.as_view(), name='main'),

]
