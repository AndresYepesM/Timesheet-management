from django.contrib import admin
from user.models import Doctor, Location, Sector

# Register your models here.

admin.site.register(Doctor)
admin.site.register(Location)
admin.site.register(Sector)