from modeltranslation.translator import register, TranslationOptions
from .models import kodeks, management, news, photo_gallery_models, service, video_data, \
    organization, about_archive


@register(kodeks.KODEKS)
class KodeksTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(management.Management)
class ManagementTranslationOptions(TranslationOptions):
    fields = ('full_name', 'position', 'clas_chin')


@register(management.ManagementEducation)
class ManagementEducationTranslationOptions(TranslationOptions):
    fields = ('place', 'specialization')


@register(management.ManagementWork)
class ManagementWorkTranslationOptions(TranslationOptions):
    fields = ('place', 'position')


@register(news.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(photo_gallery_models.PhotoGallery)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(service.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'status')


@register(video_data.VideoData)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(organization.Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(video_data.VideoLink)
class VideoLinkTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(photo_gallery_models.PhotoHome)
class PhotoHomeTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(service.PriceList)
class PriceListTranslationOptions(TranslationOptions):
    fields = ('file',)


@register(about_archive.AboutArchive)
class AboutArchiveTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
