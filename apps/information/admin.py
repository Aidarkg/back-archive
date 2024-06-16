from django.contrib import admin
from modeltranslation.admin import TranslationTabularInline
from apps.common.admin.mixins import BaseAdminMixin
from apps.information.models import News, PhotoGallery, VideoData, Management, Service, KODEKS, AboutArchive, \
    Organization, ManagementWork, ManagementEducation, Photo, VideoLink, Logo, PhotoHome, PriceList, Emblem


class VideoDataAdmin(BaseAdminMixin):
    list_display = ['title', 'video', 'public_date']
    fields = ['video', 'title', 'public_date']


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 25
    verbose_name_plural = 'Фотографии'


class PhotoGalleryAdmin(BaseAdminMixin):
    list_display = ['title', 'picture', 'public_date']
    fields = ['title', 'description', 'picture', 'public_date']
    list_display_links = ['title']
    inlines = [PhotoInline]


class NewsAdmin(BaseAdminMixin):
    list_display = ['title', 'image', 'public_date']
    fields = ['title', 'description', 'image', 'public_date']


class ManagementWorkInline(TranslationTabularInline):
    model = ManagementWork
    extra = 2
    verbose_name_plural = 'Деятельность'


class ManagementEducationInline(TranslationTabularInline):
    model = ManagementEducation
    extra = 2
    verbose_name_plural = 'Образование'


class ManagementAdmin(BaseAdminMixin):
    list_display = ['full_name', 'image', 'position', 'clas_chin']
    list_display_links = ['full_name']
    search_fields = ['full_name']

    fields = ['full_name', 'image', 'position', 'start_year', 'birth_date', 'clas_chin']
    inlines = (ManagementWorkInline, ManagementEducationInline,)


class KODEKSAdmin(BaseAdminMixin):
    list_display = ['document_number', 'title', 'pdf_file', 'date_file']
    list_display_links = ['document_number', 'title']
    fields = ['document_number', 'title', 'pdf_file', 'date_file']


class OrganizationAdmin(BaseAdminMixin):
    list_display = ['title', 'logo', 'created_at', 'updated_at']
    fields = ['logo', 'title', 'link']


class ServiceAdmin(BaseAdminMixin):
    list_display = ['title', 'status', 'created_at', 'updated_at']
    fields = ['title', 'status']


class VideoLinkAdmin(BaseAdminMixin):
    list_display = ['title', 'video_link', 'public_date']
    list_display_links = ['title', 'video_link']
    fields = ['title', 'video_link', 'public_date']


class EmblemInline(admin.TabularInline):
    model = Emblem
    extra = 1
    verbose_name_plural = 'Герб'

    def get_max_num(self, request, obj=None, **kwargs):
        return 1


class LogoAdmin(admin.ModelAdmin):
    inlines = [EmblemInline]
    list_display = ['name', 'logo', 'created_at', 'updated_at']
    list_display_links = ['name']
    readonly_fields = ['name']
    fieldsets = (
        ('Баннер', {
            'fields': ('name', 'logo')
        }),
    )


class PhotoHomeAdmin(BaseAdminMixin):
    list_display = ['title', 'photo', 'created_at', 'updated_at']
    list_display_links = ['title']
    ordering = ['-created_at']
    fields = ['photo', 'title', 'description']


class PriceListAdmin(BaseAdminMixin):
    list_display = ['title', 'file', 'created_at', 'updated_at']
    list_display_links = ['title']
    fields = ['title', 'file']
    readonly_fields = ['title', 'file']

    def has_add_permission(self, request):
        return False


class AboutArchiveAdmin(BaseAdminMixin):
    list_display = ['title', 'photo']
    fields = ['photo', 'title', 'description']


admin.site.register(News, NewsAdmin)
admin.site.register(VideoData, VideoDataAdmin)
admin.site.register(PhotoGallery, PhotoGalleryAdmin)
admin.site.register(Management, ManagementAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(KODEKS, KODEKSAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(VideoLink, VideoLinkAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(PhotoHome, PhotoHomeAdmin)
admin.site.register(PriceList, PriceListAdmin)
admin.site.register(AboutArchive, AboutArchiveAdmin)
