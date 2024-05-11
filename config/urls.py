from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from config.yasg import urlpatterns as yasg


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.data_media.urls')),
    path('', include('apps.faq.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += yasg