from rest_framework import serializers

from .models import IpStatus
from .models import Net


class IpStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IpStatus
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class NetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Net
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
