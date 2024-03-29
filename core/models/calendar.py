from django.db import models


class Weekday(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['value']


class DayOfMonth(models.Model):
    value = models.IntegerField()

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name_plural = "Days of Month"
        ordering = ['value']


class Month(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['value']
