from django.contrib import admin
from apps.common.admin.mixins import BaseAdminMixin
from apps.data_media.models import News, PhotoGallery, VideoData, Management, Service, KODEKS, \
    Organization, ManagementWork, ManagementEducation, Photo


class VideoDataAdmin(BaseAdminMixin):
    list_display = ['title', 'description', 'public_date']
    fields = ['video', 'title', 'description', 'public_date']


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 25
    verbose_name_plural = 'Фотографии'


class PhotoGalleryAdmin(BaseAdminMixin):
    list_display = ('title', 'description', 'public_date')
    fields = ['title', 'description', 'picture', 'public_date']
    list_display_links = ('title',)
    inlines = [PhotoInline]


class NewsAdmin(BaseAdminMixin):
    list_display = ['title', 'image', 'public_date']
    fields = ['title', 'description', 'image', 'public_date']


class ManagementWorkInline(admin.TabularInline):
    model = ManagementWork
    extra = 2
    verbose_name_plural = 'Деятельность'


class ManagementEducationInline(admin.TabularInline):
    model = ManagementEducation
    extra = 2
    verbose_name_plural = 'Образование'


class ManagementAdmin(BaseAdminMixin):
    list_display = ('full_name', 'image', 'position', 'created_at', 'updated_at')
    list_display_links = ('full_name',)
    search_fields = ('full_name',)

    fields = ('full_name', 'image', 'position', 'start_year', 'birth_date', 'clas_chin')
    inlines = (ManagementWorkInline, ManagementEducationInline,)


class KODEKSAdmin(BaseAdminMixin):
    list_display = ['document_number', 'title', 'pdf_file', 'date_file']
    list_display_links = ('document_number', 'title')
    fields = ['document_number', 'title', 'pdf_file', 'date_file']


class OrganizationAdmin(BaseAdminMixin):
    list_display = ['title', 'created_at', 'updated_at']
    fields = ['title', 'logo']


class ServiceAdmin(BaseAdminMixin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    fields = ['title', 'status']


admin.site.register(News, NewsAdmin)
admin.site.register(VideoData, VideoDataAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(KODEKS, KODEKSAdmin)
admin.site.register(Organization, OrganizationAdmin)
