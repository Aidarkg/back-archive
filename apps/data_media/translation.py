from modeltranslation.translator import register, TranslationOptions
from .models import kodeks, management, news, photo_gallery_models, service, video_data, \
    organization


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
    fields = ('title', 'description')


@register(service.Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'status')


@register(video_data.VideoData)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'description')


@register(organization.Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('title',)
