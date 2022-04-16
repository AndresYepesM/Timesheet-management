# from calendar import day_abbr
# from tabnanny import verbose
# from django.db import models
# from django.contrib.auth.models import User
# from user.models import Doctor

# # Create your models here.


# class Workday(models.Model):
#     day = models.DateField(auto_now_add=True)
#     clock_in = models.TimeField()
#     clock_out = models.TimeField(null=True, blank=True)

#     class Meta:
#         verbose_name_plural = 'Work day'

#     def __str__(self):
#         return f'{self.day} clock in: {self.clock_in}, clock out: {self.clock_out}'


# class Timesheet(models.Model):
#     employee = models.OneToOneField(Doctor, on_delete=models.CASCADE)
#     record = models.ForeignKey(Workday, on_delete=models.CASCADE)

#     class Meta:
#         verbose_name_plural = 'Timesheet records'

#     def __str__(self):
#         return f'{self.id}.) {self.doctor.user.first_name} {self.doctor.user.last_name}'
