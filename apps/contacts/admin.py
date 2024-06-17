from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline
from apps.contacts.models import Anticore, ArchiveContact, CollCenter, Reception, ReadingRoom, Schedule, Contact
from apps.common.admin.mixins import BaseAdminMixin


class ReceptionAdmin(TranslationStackedInline):
    model = Reception
    extra = 1
    verbose_name_plural = 'Приём граждан'


class ReadingRoomAdmin(TranslationStackedInline):
    model = ReadingRoom
    extra = 1
    verbose_name_plural = 'Читальный зал'


class ScheduleAdmin(TranslationStackedInline):
    model = Schedule
    extra = 1
    verbose_name_plural = 'График работы'


class ArchiveContactAdmin(BaseAdminMixin):
    list_display = ('location', 'phone_number', 'email')
    fields = ('location', 'phone_number', 'email')
    list_display_links = ('location', 'phone_number', 'email')
    search_fields = ('location',)

    inlines = [ReceptionAdmin, ReadingRoomAdmin, ScheduleAdmin]


class CollCenterAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)
    search_fields = ('number',)
    fields = ('number',)
    list_filter = ('created_at', 'updated_at')


class AnticoreAdmin(BaseAdminMixin):
    list_display = ('location', 'phone_number', 'email')
    fields = ('location', 'phone_number', 'email')
    list_display_links = ('location', 'phone_number', 'email')
    search_fields = ('location',)


class ContactAdmin(BaseAdminMixin):
    list_display = ('address', 'phone_number', 'index', 'fax', 'email', 'facebook')
    list_display_links = ('address', 'phone_number')
    search_fields = ('address', 'phone_number')
    fields = ('address', 'phone_number', 'index', 'fax', 'email', 'facebook')


admin.site.register(ArchiveContact, ArchiveContactAdmin)
admin.site.register(CollCenter, CollCenterAdmin)
admin.site.register(Anticore, AnticoreAdmin)
admin.site.register(Contact, ContactAdmin)
