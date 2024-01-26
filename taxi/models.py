from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=240, unique=True)


class Manufacturer(models.Model):
    name = models.CharField(max_length=240, unique=True)
    country = models.CharField(max_length=240)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=240)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"