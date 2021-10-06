from rest_framework import serializers

from .models import BackupMethod
from .models import Backup
from .models import TargetDevice
from .models import NotificationFromBackup
from .models import Notification
from .models import NotificationType


class BackupMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackupMethod
        fields = '__all__'


class BackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Backup
        fields = '__all__'


class TargetDeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = TargetDevice
        fields = '__all__'


class NotificationFromBackupSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationFromBackup
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationType
        fields = '__all__'
