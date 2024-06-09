from django.test import TestCase
from apps.contacts.models import CollCenter


class CollCenterModelTest(TestCase):

    def setUp(self):
        self.coll_center = CollCenter.objects.create(
            number="+1234567890"
        )

    def test_coll_center_creation(self):
        self.assertIsInstance(self.coll_center, CollCenter)
        self.assertEqual(self.coll_center.number, "+1234567890")

    def test_str_method(self):
        self.assertEqual(str(self.coll_center), "+1234567890")

    def test_verbose_name(self):
        self.assertEqual(CollCenter._meta.verbose_name, 'Колл-центр')
        self.assertEqual(CollCenter._meta.verbose_name_plural, 'Колл-центр')
