from rest_framework import serializers

from .models import Weekday
from .models import Month
from .models import DayOfMonth
from .models import HoursInDay
from .models import MinutesInHour


class WeekdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Weekday
        fields = '__all__'


class MonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = Month
        fields = '__all__'


class DayOfMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = DayOfMonth
        fields = '__all__'


class HoursInDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = HoursInDay
        fields = '__all__'


class MinutesInHourSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinutesInHour
        fields = '__all__'
