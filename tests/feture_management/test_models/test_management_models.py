from django.test import TestCase
from apps.information.models.management import Management, ManagementEducation, ManagementWork


class ManagementTestCase(TestCase):
    def setUp(self):
        self.management = Management.objects.create(
            full_name='John Doe',
            image='john_doe.jpg',
            position='CEO',
            start_year=2020,
            birth_date='1990-01-01',
            clas_chin='First Class'
        )

    def test_end_year(self):
        self.assertEqual(self.management.end_year, 2024)  # Assuming the current year is 2024

    def test_str_representation(self):
        self.assertEqual(str(self.management), 'John Doe')

    def test_verbose_names(self):
        # Test verbose names
        self.assertEqual(Management._meta.verbose_name, 'Руководство')
        self.assertEqual(Management._meta.verbose_name_plural, 'Руководства')
        self.assertEqual(Management._meta.get_field('full_name').verbose_name, 'полное имя')
        self.assertEqual(Management._meta.get_field('image').verbose_name, 'фотография')
        self.assertEqual(Management._meta.get_field('position').verbose_name, 'Должность')
        self.assertEqual(Management._meta.get_field('start_year').verbose_name, 'Год начала работы')
        self.assertEqual(Management._meta.get_field('birth_date').verbose_name, 'Дата рождения')
        self.assertEqual(Management._meta.get_field('clas_chin').verbose_name, 'Классный чин')

    def test_created_at_ordering(self):
        self.assertIn(('-created_at'), Management._meta.ordering)


class ManagementEducationTestCase(TestCase):
    def setUp(self):
        self.management = Management.objects.create(
            full_name='John Doe',
            image='john_doe.jpg',
            position='CEO',
            start_year=2020,
            birth_date='1990-01-01',
            clas_chin='First Class'
        )
        self.management_education = ManagementEducation.objects.create(
            year=2010,
            place='University of Example',
            specialization='Computer Science',
            management=self.management
        )

    def test_management_education_relationship(self):
        self.assertEqual(self.management.managements_education.first(), self.management_education)


class ManagementWorkTestCase(TestCase):
    def setUp(self):
        self.management = Management.objects.create(
            full_name='John Doe',
            image='john_doe.jpg',
            position='CEO',
            start_year=2020,
            birth_date='1990-01-01',
            clas_chin='First Class'
        )
        self.management_work = ManagementWork.objects.create(
            year='2010-2020',
            place='Example Company',
            position='Software Engineer',
            management=self.management
        )

    def test_management_work_relationship(self):
        self.assertEqual(self.management.managements_work.first(), self.management_work)


