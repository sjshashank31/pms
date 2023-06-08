from django.db import models
from django.conf import settings
import datetime
from django.core.exceptions import ValidationError
# Create your models here.

class CommonStampModel(models.Model):
    """
    This should be placed into a common app
    it will be used for added_by, updated_by, added_on, updated_on field.

    """
    added_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                 related_name="%(class)s_common_added_by", limit_choices_to={'is_staff': True},
                                 on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True,
                                    related_name="%(class)s_common_modified_by", limit_choices_to={'is_staff': True},
                                    on_delete=models.SET_NULL)

class Building(CommonStampModel):
    """
    Buidlings should be different App
    It should have state a foreign key from State model
    It should have country foreign key from Country Model
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=1026)
    resident_manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


class Employee(CommonStampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Resident(CommonStampModel):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=10, unique=True)
    image = models.ImageField(upload_to='users/img', null=True, blank=True)
    aadhar_card_no = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    location = models.ForeignKey(Building, on_delete=models.CASCADE)
    rent_amount = models.IntegerField()
    token_amount = models.IntegerField()
    contract_start_date = models.DateField(null=True, blank=True)
    contract_end_date = models.DateField(null=True, blank=True)
    move_in_date = models.DateField(null=True, blank=True)
    move_out_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.date_of_birth and  self.date_of_birth>datetime.date.today():
            raise ValidationError("Date of birth Should be less than or Equals to today's date")



