from django.test import TestCase
from apps.contacts.models import Anticore


class AnticoreModelTest(TestCase):

    def setUp(self):
        self.anticore = Anticore.objects.create(
            location="123 Главная ул., Город, Страна",
            phone_number="+1234567890",
            email="test@example.com"
        )

    def test_anticore_creation(self):
        self.assertIsInstance(self.anticore, Anticore)
        self.assertEqual(self.anticore.location, "123 Главная ул., Город, Страна")
        self.assertEqual(self.anticore.phone_number, "+1234567890")
        self.assertEqual(self.anticore.email, "test@example.com")

    def test_str_method(self):
        self.assertEqual(str(self.anticore), "123 Главная ул., Город, Страна")

    def test_verbose_name(self):
        self.assertEqual(Anticore._meta.verbose_name, 'Антикоррупционные дела')
        self.assertEqual(Anticore._meta.verbose_name_plural, 'Антикоррупционные дела')
