from rest_framework import serializers

from .models import UserLicense
from .models import ComputerLicense
from .models import LicenseWithUser
from .models import LicenseWithComputer


class UserLicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLicense
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerLicenseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerLicense
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class LicenseWithUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LicenseWithUser
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class LicenseWithComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LicenseWithComputer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
