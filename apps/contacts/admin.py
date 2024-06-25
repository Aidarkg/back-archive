from django.contrib import admin
from modeltranslation.admin import TranslationStackedInline
from apps.contacts.models import Anticore, ArchiveContact, CollCenter, Reception, ReadingRoom, Schedule, Contact
from apps.common.admin.mixins import BaseAdminMixin


class ReceptionAdmin(TranslationStackedInline):
    model = Reception
    extra = 1
    verbose_name_plural = 'Приём граждан'

    def get_max_num(self, request, obj=None, **kwargs):
        return 1


class ReadingRoomAdmin(TranslationStackedInline):
    model = ReadingRoom
    extra = 1
    verbose_name_plural = 'Читальный зал'

    def get_max_num(self, request, obj=None, **kwargs):
        return 1


class ScheduleAdmin(TranslationStackedInline):
    model = Schedule
    extra = 1
    verbose_name_plural = 'График работы'

    def get_max_num(self, request, obj=None, **kwargs):
        return 1


class ArchiveContactAdmin(BaseAdminMixin):
    list_display = ('location', 'phone_number', 'email')
    fields = ('location', 'phone_number', 'email')
    list_display_links = ('location', 'phone_number', 'email')
    search_fields = ('location',)

    inlines = [ReceptionAdmin, ReadingRoomAdmin, ScheduleAdmin]

    def has_add_permission(self, request):
        if ArchiveContact.objects.all().count() == 1:
            return False
        else:
            return True


class CollCenterAdmin(admin.ModelAdmin):
    list_display = ('number',)
    list_display_links = ('number',)
    search_fields = ('number',)
    fields = ('number',)
    list_filter = ('created_at', 'updated_at')

    def has_add_permission(self, request):
        if CollCenter.objects.all().count() == 1:
            return False
        else:
            return True


class AnticoreAdmin(BaseAdminMixin):
    list_display = ('location', 'phone_number', 'email')
    fields = ('location', 'phone_number', 'email')
    list_display_links = ('location', 'phone_number', 'email')
    search_fields = ('location',)

    def has_add_permission(self, request):
        if Anticore.objects.all().count() == 1:
            return False
        else:
            return True


class ContactAdmin(BaseAdminMixin):
    list_display = ('address', 'phone_number', 'index', 'fax', 'email', 'facebook')
    list_display_links = ('address', 'phone_number')
    search_fields = ('address', 'phone_number')
    fields = ('address', 'phone_number', 'index', 'fax', 'email', 'facebook')

    def has_add_permission(self, request):
        if Contact.objects.all().count() == 1:
            return False
        else:
            return True


admin.site.register(ArchiveContact, ArchiveContactAdmin)
admin.site.register(CollCenter, CollCenterAdmin)
admin.site.register(Anticore, AnticoreAdmin)
admin.site.register(Contact, ContactAdmin)
