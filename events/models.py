import datetime

from django.db import models
from users.models import CommonStampModel, Building
from django.core.exceptions import ValidationError
# Create your models here.


class Event(CommonStampModel):
    """
    Events Can be created by community manager for a particular day
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    location = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='event_building')

    def __str__(self):
        return self.name

    def clean(self):
        if self.date<datetime.date.today():
            raise ValidationError("Date Should be greater or Equals to today's date")


