from django.contrib import admin
from apps.common.admin.mixins import BaseAdminMixin
from apps.data_media.models import News, PhotoGallery, VideoData, Management, Service, KODEKS, Contact, Visit, \
    Organization, ManagementWork, ManagementEducation, Photo


class VideoDataAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'description', 'created_at', 'updated_at']
    fields = ['video', 'title', 'description']


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 25
    verbose_name_plural = 'Фотографии'


class PhotoGalleryAdmin(BaseAdminMixin):
    list_display = ('id', 'title', 'description', 'created_at', 'updated_at')
    fields = ['title', 'description', 'picture']
    list_display_links = ('id', 'title')
    inlines = [PhotoInline]


class NewsAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'description', 'detailed_description', 'image', 'public_date']
    fields = ['title', 'description', 'detailed_description', 'image', 'public_date']


class ManagementWorkInline(admin.TabularInline):
    model = ManagementWork
    extra = 2
    verbose_name_plural = 'Деятельность'


class ManagementEducationInline(admin.TabularInline):
    model = ManagementEducation
    extra = 2
    verbose_name_plural = 'Образование'


class ManagementAdmin(BaseAdminMixin):
    list_display = ('id', 'full_name', 'image', 'position', 'created_at', 'updated_at')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name',)

    fields = ('full_name', 'image', 'position', 'birth_date', 'clas_chin')
    inlines = (ManagementWorkInline, ManagementEducationInline,)


class KODEKSAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'pdf_file', 'created_at', 'updated_at']
    fields = ['title', 'pdf_file']


class ContactAdmin(BaseAdminMixin):
    list_display = ['id', 'address', 'phone', 'email', 'work_time', 'reception', 'reading_room', 'created_at',
                    'updated_at']
    list_display_links = ['id', 'address']
    search_fields = ['address']
    fields = ['address', 'phone', 'email', 'work_time', 'reception', 'reading_room']


class VisitAdmin(BaseAdminMixin):
    list_display = ['id', 'date', 'count']
    list_display_links = ['id', 'date']
    search_fields = ['date']
    fields = ['date', 'count']


class OrganizationAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'created_at', 'updated_at']
    fields = ['title', 'logo']


class ServiceAdmin(BaseAdminMixin):
    list_display = ['id', 'title', 'status', 'created_at', 'updated_at']
    fields = ['title', 'status']


admin.site.register(News, NewsAdmin)
admin.site.register(VideoData, VideoDataAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(KODEKS, KODEKSAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Organization, OrganizationAdmin)
# admin.site.register(Visit, VisitAdmin)
