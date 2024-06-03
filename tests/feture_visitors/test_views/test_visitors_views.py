from django.test import TestCase, RequestFactory
from rest_framework.test import APIClient
from apps.information.models import Visitors
from apps.information.views import VisitorsAPIView


class VisitorsAPIViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_visitors_api_view(self):

        request = self.factory.get('/visitors/')


        view = VisitorsAPIView.as_view()


        response = view(request)


        self.assertEqual(response.status_code, 200)


        self.assertIn('counter', response.data)


        self.assertIsInstance(response.data['counter'], int)


    def test_visitors_api_view_increment_counter(self):

        visitor = Visitors.objects.create(pk=1)
        initial_counter = visitor.counter


        request = self.factory.get('/visitors/')


        response = VisitorsAPIView.as_view()(request)


        self.assertEqual(response.status_code, 200)


        visitor.refresh_from_db()
        self.assertEqual(visitor.counter, initial_counter + 1)