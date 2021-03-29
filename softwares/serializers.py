from rest_framework import serializers

from .models import OperatingSystem
from .models import SoftwareArchitecture
from .models import SoftwareCategory
from .models import Software


class OperatingSystemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class SoftwareArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftwareArchitecture
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class SoftwareCategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoftwareCategory
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class SoftwareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Software
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
