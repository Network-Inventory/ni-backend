from rest_framework import serializers

from .models import User
from .models import UserInAdGroup
from .models import UserInMailGroup
from .models import AdGroup
from .models import MailGroup
from .models import MailAlias


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class UserInAdGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInAdGroup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class UserInMailGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInMailGroup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class AdGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AdGroup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class MailGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailGroup
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class MailAliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailAlias
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])






