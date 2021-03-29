from rest_framework import serializers

from .models import Weekday
from .models import Month
from .models import DayOfMonth
from .models import HoursInDay
from .models import MinutesInHour


class WeekdaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weekday
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class MonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Month
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class DayOfMonthSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DayOfMonth
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class HoursInDaySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HoursInDay
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])


class MinutesInHourSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MinutesInHour
        fields = [field.name for field in model._meta.fields]
        fields.extend(['id', 'url'])
