from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Doctor(models.Model):
    isDoctor = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ssn = models.IntegerField(unique=True, verbose_name='Social security number')
    home_address = models.CharField(max_length=65, verbose_name='Home address')
    phone_num = models.CharField(max_length=15, verbose_name='Phone number')
    specialty = models.CharField(max_length=65, verbose_name='Specialty fo the doctor')
    office_address = models.CharField(max_length=150, verbose_name='Office address')
    isWest = models.BooleanField(blank=True, verbose_name='is from west?')
    isEast = models.BooleanField(blank=True, verbose_name='is from east?')

    class Meta:
        verbose_name_plural = 'Doctors'

    def __str__(self):
        return f'{self.user.id}.) {self.user.first_name} {self.user.last_name}'


class Location(models.Model):
    name = models.CharField(max_length=125, verbose_name='Name of the location')
    isWest = models.BooleanField(blank=True, verbose_name='is from west?')
    isEast = models.BooleanField(blank=True, verbose_name='is from east?')
    isActive = models.BooleanField(default=True, blank=True, null=True, verbose_name='still active?')
    address = models.CharField(max_length=125, verbose_name='Address of the location')

    class Meta:
        verbose_name_plural = 'Locations available'

    def __str__(self):
        return f'{self.name} -- {self.address}'
