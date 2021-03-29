from rest_framework import serializers

from .models import Owner
from .models import Customer
from .models import DeviceManufacturer
from .models import Location


class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DeviceManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceManufacturer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
