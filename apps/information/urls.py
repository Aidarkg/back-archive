from django.urls import path
from apps.information.views import VideoDataAPIView, \
    NewsListAPIView, NewsDetailAPIView, \
    PhotoGalleryListAPIView, PhotoGalleryDetailAPIView, \
    ServiceListView, PriceListAPIView, \
    KODEKSListCreateAPIView, KODEKSRetrieveUpdateDestroyAPIView, \
    SearchAPIView, AboutArchiveAPIView, \
    VisitorsAPIView, EmblemAPIView, \
    ManagementListAPIView, ManagementDetailAPIView, \
    MainAPIView, PhotoHomeDetailAPIView, PhotoHomeListAPIView
from apps.information.views.organization import OrganizationListView


urlpatterns = [
    path('video/', VideoDataAPIView.as_view(), name='video-data-list'),
    path('management/', ManagementListAPIView.as_view(), name='management-list'),
    path('management/<int:pk>/', ManagementDetailAPIView.as_view(), name='management-detail'),
    path('news/', NewsListAPIView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDetailAPIView.as_view(), name='news-detail'),
    path('photos/', PhotoGalleryListAPIView.as_view(), name='photo-gallery-list'),
    path('photos/<int:pk>/', PhotoGalleryDetailAPIView.as_view(), name='photo-gallery-detail'),
    path('photo_home/', PhotoHomeListAPIView.as_view(), name='photo-home-list'),
    path('photo_home/<int:pk>/', PhotoHomeDetailAPIView.as_view(), name='photo-home-detail'),
    path('service/', ServiceListView.as_view(), name='services-list'),
    path('service_price/', PriceListAPIView.as_view(), name='price-list'),
    path('kodeks/', KODEKSListCreateAPIView.as_view(), name='kodeks-list'),
    path('kodeks/<int:pk>/', KODEKSRetrieveUpdateDestroyAPIView.as_view(), name='kodeks-detail'),
    path('search/', SearchAPIView.as_view(), name='search'),
    path('visitors/', VisitorsAPIView.as_view(), name='visitors-list'),
    path('organizations/', OrganizationListView.as_view(), name='organizations'),
    path('main/', MainAPIView.as_view(), name='main'),
    path('emblem/', EmblemAPIView.as_view(), name='emblem'),
    path('about_archive/', AboutArchiveAPIView.as_view(), name='about-archive'),

]
