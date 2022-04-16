from django.db import models
from django.contrib.auth.models import User
from user.models import Doctor, Location

# Create your models here.

class Timecard(models.Model):
    workday = models.DateField(auto_now_add=True)
    clock_in = models.TimeField()
    clock_out = models.TimeField(null=True, blank=True)
    employee = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    zone = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Timecards'
    
    def __str__(self):
        return f'{self.workday} {self.employee.user.first_name}'