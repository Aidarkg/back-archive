import os
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
django.setup()

from django.utils import timezone
from apps.information.models import KODEKS, Management, News, VideoData, PhotoGallery, Service, Organization, \
    Photo, VideoLink
from apps.moderator.models import Moderator
from django.contrib.auth import get_user_model

start_time = time.time()

# import datetime
#
# current_year = datetime.datetime.now().year
# print(type(current_year))


# KODEKS.objects.all().delete()
# Management.objects.all().delete()
# News.objects.all().delete()
# VideoData.objects.all().delete()
# PhotoGallery.objects.all().delete()
# Contact.objects.all().delete()
# Service.objects.all().delete()
# Organization.objects.all().delete()
# Moderator.objects.all().delete()

# create kodeks
# for i in range(20):
#     KODEKS.objects.create(
#         title='Закон о содействии занятости населения',
#         title_ru='Закон о содействии занятости населения',
#         title_en='The Law on Public Assistance',
#         title_ky='Калкка комоктошуу мыйзамы',
#         pdf_file='pdf_files/ПИ.pdf',
#         date_file=timezone.now().date(),
#         document_number=i
#     )

# create news
for i in range(15):
    News.objects.create(
        title='Садыр Жапаров выпустил приказ по созданию общегосударственной архивной службы',
        title_ky='Садыр Жапаров жалпы мамлекеттик архив кызматын түзүү боюнча буйрук чыгарды',
        title_en='Sadyr Zhaparov issued an order to create a nationwide archival service',
        title_ru='Садыр Жапаров выпустил приказ по созданию общегосударственной архивной службы',
        public_date=timezone.now().date(),
        description='Президент Садыр Жапаров подписал Указ «О создании благоприятной налоговой '
                    'среды для субъектов предпринимательства и повышении заинтересованности застрахованных '
                    'лиц в государственном социальном обеспечении». Об этом сообщили в пресс-службе главы государства.',
        description_ky='Президент Садыр Жапаров "ишкердик субъекттери үчүн жагымдуу салык чөйрөсүн түзүү жана '
                       'камсыздандырылган адамдардын мамлекеттик социалдык камсыздоого кызыкчылыгын жогорулатуу '
                       'жөнүндө"Жарлыкка кол койду. Бул тууралуу мамлекет башчынын басма сөз кызматы билдирди.',
        description_en='President Sadyr Zhaparov signed a decree "On creating a favorable tax environment for business '
                       'entities and increasing the interest of insured persons in state social security." This was '
                       'reported in the press service of the head of state.',
        description_ru='Президент Садыр Жапаров подписал Указ «О создании благоприятной налоговой '
                        'среды для субъектов предпринимательства и повышении заинтересованности застрахованных '
                        'лиц в государственном социальном обеспечении». Об этом сообщили в пресс-службе главы государства.',
        image='news/public3.png'
    )

# create video gallery
for i in range(15):
    VideoData.objects.create(
        video='video/archive.mp4',
        title='Архив документ',
        title_ky='Архивдик документ',
        title_en='Archive document',
        title_ru='Архив документ',
        public_date=timezone.now().date()
    )

# create photo gallery
for i in range(20):
    gallery = PhotoGallery.objects.create(
        picture='gallery/logo/Снимок_экрана_от_2024-06-11_22-53-46.png',
        title='Архив президента',
        title_ky='Президенттин архиви',
        title_en='President archive',
        title_ru='Архив президента',
        description='Президенттин архиви',
        description_ky='Архив президента',
        description_en='President archive',
        description_ru='Архив президента',
        public_date=timezone.now().date()
    )
    for j in range(24):
        Photo.objects.create(
            gallery=gallery,
            photo=f'gallery/photos/Снимок_экрана_от_2024-06-11_22-53-46.png'
        )

#create video_link
# for i in range(20)

# create contacts
# for i in range(200):
# Contact.objects.create(
#     address='г. Бишкек, Первомайский район, улица Месароша 205',
#     address_ky='Бишкек, Первомайский район, улица Месароша 205',
#     address_en='Bishkek, Pervomaisky district, 205 Mesarosha Street',
#     address_ru='г. Бишкек, Первомайский район, улица Месароша 205',
#     phone='+996500123456',
#     email='archive@gmail.com',
#     reading_room='Читальный зал',
#     reading_room_ky='Окуучу болмо',
#     reading_room_en='Reading room',
#     reading_room_ru='Читальный зал',
#     work_time='8:00-15:00',
#     reception='Прием граждан',
#     reception_ky='Жарандарды алуу',
#     reception_en='Reception',
#     reception_ru='Прием граждан',
#     )

# create service
for i in range(100):
    Service.objects.create(
        title='Предоставление копий документов из архивного фонда',
        title_ky='Архивдын фонддогу документтердин копияларын жөнөтуу',
        title_en='Copying of documents from the archives',
        title_ru='Предоставление копий документов из архивного фонда',
        status='Платно',
        status_ky='Акылуу',
        status_en='Paid',
        status_ru='Платно'
    )

# create organizations
for i in range(10):
    Organization.objects.create(
        title='Жогорку Кенеш Кыргызской Республики',
        title_ky='Кыргыз Республикасынын Жогорку Кенеши',
        title_en='Jogorku Kenesh Kyrgyz Republic',
        title_ru='Жогорку Кенеш Кыргызской Республики',
        logo='logo/Logo_of_the_Jogorku_Kenesh.png',
        link='https://kenesh.kg/ru'
    )

# create moderators
# for i in range(500):
#     Moderator.objects.create(
#         username='Moderator',
#         email='moderator@gmail.com',
#         group_id=1
#     )

# create photos
# for i in range()


end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")
