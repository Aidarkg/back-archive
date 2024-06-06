from django.test import TestCase
from apps.information.models import Visitors
from apps.information.serializers import VisitorSerializer

class VisitorSerializerTestCase(TestCase):
    def setUp(self):
        self.visitor_data = {'counter': 10}
        self.visitor = Visitors.objects.create(counter=self.visitor_data['counter'])
        self.serializer = VisitorSerializer(instance=self.visitor)

    def test_serializer_contains_expected_fields(self):
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['counter']))

    def test_serializer_fields_content(self):
        data = self.serializer.data
        self.assertEqual(data['counter'], self.visitor_data['counter'])

    def test_create_visitor_with_serializer(self):
        new_counter = 20
        serializer = VisitorSerializer(data={'counter': new_counter})
        self.assertTrue(serializer.is_valid())
        visitor = serializer.save()
        self.assertIsInstance(visitor, Visitors)
        self.assertEqual(visitor.counter, new_counter)
