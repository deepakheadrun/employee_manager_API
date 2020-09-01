from .models import InterestedArea
from rest_framework import serializers


class InterestedAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestedArea
        fields = '__all__'

