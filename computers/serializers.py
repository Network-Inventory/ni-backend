from rest_framework import serializers

from .models import Computer
from .models import ComputerCpuRelation
from .models import ComputerDiskRelation
from .models import ComputerGpuRelation
from .models import ComputerRamRelation
from .models import ComputerSoftwareRelation
from .models import CpuArchitecture
from .models import CpuManufacturer
from .models import Cpu
from .models import DiskType
from .models import Disk
from .models import GpuManufacturer
from .models import Gpu
from .models import DisksInRaid
from .models import RaidType
from .models import Raid
from .models import RamType
from .models import Ram


class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = '__all__'
        depth = 1


class ComputerCpuRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerCpuRelation
        fields = '__all__'


class ComputerDiskRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerDiskRelation
        fields = '__all__'


class ComputerGpuRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerGpuRelation
        fields = '__all__'


class ComputerRamRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerRamRelation
        fields = '__all__'


class ComputerSoftwareRelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComputerSoftwareRelation
        fields = '__all__'


class CpuArchitectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuArchitecture
        fields = '__all__'


class CpuManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuManufacturer
        fields = '__all__'


class CpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cpu
        fields = '__all__'


class DiskTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiskType
        fields = '__all__'


class DiskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disk
        fields = '__all__'


class GpuManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpuManufacturer
        fields = '__all__'


class GpuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gpu
        fields = '__all__'


class DisksInRaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisksInRaid
        fields = '__all__'


class RaidTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RaidType
        fields = '__all__'


class RaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Raid
        fields = '__all__'


class RamTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamType
        fields = '__all__'


class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ram
        fields = '__all__'
