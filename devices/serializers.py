from rest_framework import serializers

from .models import Warranty
from .models import WarrantyType
from .models import Device
from .models import DeviceCategory
from .models import DeviceInNet
from .models import DeviceManufacturer
from .models import HardwareModel


class WarrantySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Warranty
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class WarrantyTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WarrantyType
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Device
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DeviceCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceCategory
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DeviceInNetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceInNet
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DeviceManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DeviceManufacturer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class HardwareModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HardwareModel
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
