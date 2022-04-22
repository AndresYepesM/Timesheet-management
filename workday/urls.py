from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from workday.views import *

urlpatterns = [
    re_path(r'^timecard/activity/(?P<pk>\d+)$',TodayActivity, name='activity'),

    path('timecard/clock_in/', login_required(ClockInMethod.as_view()), name='Clock_in'),

    re_path(r'^timecard/clock_out/(?P<slug>\d+)$',login_required(ClockOutMethod.as_view()), name='Clock_out'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)