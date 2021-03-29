from rest_framework import serializers

from .models import BackupMethod
from .models import Backup
from .models import TargetDevice
from .models import NotificationFromBackup
from .models import Notification
from .models import NotificationType


class BackupMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BackupMethod
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class BackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Backup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class TargetDeviceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TargetDevice
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class NotificationFromBackupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationFromBackup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class NotificationTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NotificationType
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
