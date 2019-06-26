from django.db import models
from django.contrib.gis.db import models as gis_models
from languages.fields import LanguageField
from phonenumber_field.modelfields import PhoneNumberField


class Provider(models.Model):
    name = models.CharField(null=False, blank=False, max_length=100)
    email = models.EmailField(null=False, blank=False, unique=True)
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    language = LanguageField()


class ServiceArea(models.Model):
    provider = Provider()
    name = models.CharField(null=False, blank=False, max_length=100)
    area = gis_models.PolygonField()
