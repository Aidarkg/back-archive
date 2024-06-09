from django.test import TestCase
from apps.contacts.models import Contact


class ContactModelTest(TestCase):

    def setUp(self):
        self.contact = Contact.objects.create(
            address="123 Main St, City, Country",
            phone_number="+1234567890",
            index="123456",
            fax="+1234567891",
            email="test@example.com",
            facebook="https://www.facebook.com/test"
        )

    def test_contact_creation(self):
        self.assertIsInstance(self.contact, Contact)
        self.assertEqual(self.contact.address, "123 Main St, City, Country")
        self.assertEqual(self.contact.phone_number, "+1234567890")
        self.assertEqual(self.contact.index, "123456")
        self.assertEqual(self.contact.fax, "+1234567891")
        self.assertEqual(self.contact.email, "test@example.com")
        self.assertEqual(self.contact.facebook, "https://www.facebook.com/test")

    def test_str_method(self):
        self.assertEqual(str(self.contact), "123 Main St, City, Country")

    def test_verbose_name(self):
        self.assertEqual(Contact._meta.verbose_name, 'Контакты')
        self.assertEqual(Contact._meta.verbose_name_plural, 'Контакты')

    def test_ordering(self):
        self.assertEqual(Contact._meta.ordering, ['-created_at'])
