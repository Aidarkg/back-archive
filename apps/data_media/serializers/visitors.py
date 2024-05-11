from rest_framework import serializers


class VisitSerializer(serializers.Serializer):
    total_visits = serializers.IntegerField()
    today_visits = serializers.IntegerField()
