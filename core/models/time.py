from django.db import models


class HoursInDay(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "Hours"
        ordering = ['value']


class MinutesInHour(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "Minutes"
        ordering = ['value']
