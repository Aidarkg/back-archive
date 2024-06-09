from django.test import TestCase
from django.utils import timezone
from apps.contacts.models.coll_center_models import CollCenter
from apps.contacts.serializers.general_serializers import CollCenterSerializer


class CollCenterSerializerTest(TestCase):
    def setUp(self):
        self.coll_center_data = {
            'number': '1234567890',
        }
        self.coll_center = CollCenter.objects.create(**self.coll_center_data)

    def test_coll_center_serializer(self):
        serializer = CollCenterSerializer(instance=self.coll_center)
        self.assertEqual(serializer.data['number'], self.coll_center_data['number'])
        self.assertNotIn('field_name', serializer.data)
