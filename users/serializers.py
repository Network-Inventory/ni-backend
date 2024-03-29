from rest_framework import serializers

from .models import User
from .models import UserInAdGroup
from .models import UserInMailGroup
from .models import AdGroup
from .models import MailGroup
from .models import MailAlias


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserInAdGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInAdGroup
        fields = '__all__'


class UserInMailGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInMailGroup
        fields = '__all__'


class AdGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdGroup
        fields = '__all__'


class MailGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailGroup
        fields = '__all__'


class MailAliasSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailAlias
        fields = '__all__'
