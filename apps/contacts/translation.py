from modeltranslation.translator import register, TranslationOptions
from apps.contacts.models import ArchiveContact, Reception, ReadingRoom, Schedule, Anticore, Contact


@register(ArchiveContact)
class ArchiveContactTranslationOptions(TranslationOptions):
    fields = ('location',)


@register(Reception)
class ReceptionTranslationOptions(TranslationOptions):
    fields = ('weekdays',)


@register(ReadingRoom)
class ReadingRoomTranslationOptions(TranslationOptions):
    fields = ('weekdays',)


@register(Schedule)
class ScheduleTranslationOptions(TranslationOptions):
    fields = ('weekdays', 'weekend')


@register(Anticore)
class AnticoreTranslationOptions(TranslationOptions):
    fields = ('location',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address',)
