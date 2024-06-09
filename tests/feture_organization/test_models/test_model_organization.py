from django.test import TestCase
from apps.information.models.organization import Organization


class OrganizationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Organization.objects.create(title='Test Organization', logo='logo/test_logo.png')

    def test_title_label(self):
        organization = Organization.objects.get(id=1)
        field_label = organization._meta.get_field('title').verbose_name
        self.assertEquals(field_label, 'Название организации')

    def test_logo_label(self):
        organization = Organization.objects.get(id=1)
        field_label = organization._meta.get_field('logo').verbose_name
        self.assertEquals(field_label, 'Логотип')

    def test_title_max_length(self):
        organization = Organization.objects.get(id=1)
        max_length = organization._meta.get_field('title').max_length
        self.assertEquals(max_length, 300)
