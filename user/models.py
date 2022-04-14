from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    ssn = models.IntegerField(unique=True, verbose_name='Social security number')
    home_address = models.CharField(max_length=65, verbose_name='Home address')
    phone_num = models.CharField(max_length=15, verbose_name='Phone number')
    specialty = models.CharField(max_length=65, verbose_name='Specialty fo the doctor')
    office_address = models.CharField(max_length=150, verbose_name='Office address')
    class Meta:
        verbose_name_plural = 'Doctors'
    def __str__(self):
        return f'{self.user.id}.) {self.user.first_name} {self.user.last_name}'