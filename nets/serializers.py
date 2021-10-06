from rest_framework import serializers

from .models import IpStatus
from .models import Net


class IpStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IpStatus
        fields = '__all__'


class NetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Net
        fields = '__all__'
