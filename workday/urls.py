from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from workday.views import *

urlpatterns = [

    path('timecard/', Timecard_mainpage, name='Timecard_main'),

    path('clock_in/', login_required(ClockInMethod.as_view()), name='Clock_in'),

    re_path(r'^clock_out/(?P<pk>\d+)$',login_required(ClockOutMethod.as_view()), name='Clock_out'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)