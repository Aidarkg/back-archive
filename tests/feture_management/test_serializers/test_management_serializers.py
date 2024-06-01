from datetime import datetime

from django.test import TestCase
from apps.information.models.management import Management, ManagementEducation, ManagementWork
from apps.information.serializers.management import (
    ManagementListSerializers,
    ManagementDetailsSerializers,
    ManagementEducationSerializers,
    ManagementWorkSerializer
)

class ManagementListSerializerTest(TestCase):
    def test_serializer_fields(self):
        serializer = ManagementListSerializers()
        self.assertEqual(set(serializer.fields.keys()), {'id', 'full_name', 'image', 'position', 'start_year', 'end_year'})

class ManagementEducationSerializerTest(TestCase):
    def test_serializer_fields(self):
        serializer = ManagementEducationSerializers()
        self.assertEqual(set(serializer.fields.keys()), {'year', 'place', 'specialization'})

class ManagementWorkSerializerTest(TestCase):
    def test_serializer_fields(self):
        serializer = ManagementWorkSerializer()
        self.assertEqual(set(serializer.fields.keys()), {'year', 'place', 'position'})

class ManagementDetailsSerializerTest(TestCase):
    def test_serializer_fields(self):
        serializer = ManagementDetailsSerializers()
        self.assertEqual(set(serializer.fields.keys()), {'id', 'full_name', 'image', 'position', 'birth_date', 'clas_chin', 'managements_education', 'managements_work'})

    def test_nested_serializers(self):
        current_year = datetime.now().year
        management = Management.objects.create(
            full_name='Test Name',
            position='Test Position',
            start_year=current_year
        )
        education = ManagementEducation.objects.create(year=2020, place='Test Place', specialization='Test Spec',
                                                       management=management)
        work = ManagementWork.objects.create(year='2020-2021', place='Test Work Place', position='Test Position',
                                             management=management)

        serializer = ManagementDetailsSerializers(instance=management)
        self.assertEqual(serializer.data['id'], management.id)
        self.assertEqual(serializer.data['full_name'], management.full_name)
        self.assertEqual(serializer.data['position'], management.position)
        self.assertEqual(serializer.data['birth_date'], management.birth_date)
        self.assertEqual(serializer.data['clas_chin'], management.clas_chin)
        self.assertEqual(serializer.data['managements_education'][0]['year'], education.year)
        self.assertEqual(serializer.data['managements_education'][0]['place'], education.place)
        self.assertEqual(serializer.data['managements_education'][0]['specialization'], education.specialization)
        self.assertEqual(serializer.data['managements_work'][0]['year'], work.year)
        self.assertEqual(serializer.data['managements_work'][0]['place'], work.place)
        self.assertEqual(serializer.data['managements_work'][0]['position'], work.position)