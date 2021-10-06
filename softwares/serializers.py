from rest_framework import serializers

from .models import OperatingSystem
from .models import SoftwareArchitecture
from .models import SoftwareCategory
from .models import Software


class OperatingSystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperatingSystem
        fields = '__all__'


class SoftwareArchitectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareArchitecture
        fields = '__all__'


class SoftwareCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SoftwareCategory
        fields = '__all__'


class SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Software
        fields = '__all__'
