from django.test import TestCase
from apps.information.models.visitors import Visitors

class VisitorsTestCase(TestCase):
    def setUp(self):
        self.visitor = Visitors.objects.create(counter=0)

    def test_increase_count(self):

        initial_counter = self.visitor.counter
        self.visitor.increase_count()
        self.assertEqual(self.visitor.counter, initial_counter + 1)

    def test_counter_default_value(self):

        self.assertEqual(self.visitor.counter, 0)
