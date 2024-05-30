import pdb

from rest_framework import serializers

from apps.information.models import News


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = News
        fields = ('id', 'title', 'description', 'image', 'public_date')

    def get_image(self, obj):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(obj.image.url)
        return obj.image.url
