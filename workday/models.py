from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from user.models import Doctor, Location

# Create your models here.

class Timecard(models.Model):
    employee = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    zone = models.ForeignKey(Location, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    workday = models.DateField(auto_now_add=True)
    clock_in = models.TimeField()
    clock_out = models.TimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Timecards'

    def __str__(self):
        return f'{self.slug} {self.workday} {self.employee.user.first_name}'

    
