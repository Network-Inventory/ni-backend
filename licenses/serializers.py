from rest_framework import serializers

from .models import UserLicense
from .models import ComputerLicense
from .models import LicenseWithUser
from .models import LicenseWithComputer


class UserLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLicense
        fields = '__all__'


class ComputerLicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerLicense
        fields = '__all__'


class LicenseWithUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseWithUser
        fields = '__all__'


class LicenseWithComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseWithComputer
        fields = '__all__'
