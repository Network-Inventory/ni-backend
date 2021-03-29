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


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Computer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerCpuRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerCpuRelation
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerDiskRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerDiskRelation
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerGpuRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerGpuRelation
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerRamRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerRamRelation
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class ComputerSoftwareRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ComputerSoftwareRelation
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class CpuArchitectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CpuArchitecture
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class CpuManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CpuManufacturer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class CpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cpu
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DiskTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DiskType
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DiskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Disk
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class GpuManufacturerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GpuManufacturer
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class GpuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Gpu
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DisksInRaidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DisksInRaid
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class RaidTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RaidType
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class RaidSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Raid
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class RamTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RamType
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class RamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ram
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
