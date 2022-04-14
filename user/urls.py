from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from user.views import *

urlpatterns = [
    
    path('main/', AdministrationMainPage, name='Admin_main_page'),

    path('doctors/main', login_required(DoctorsList.as_view()), name='Doctor_list'),

    re_path(r'^doctor/detail/(?P<pk>\d+)$', login_required(DoctorDetail.as_view()), name='Doctor_detail'),

    path('doctor/new_doctor', login_required(CreateNewDoctor.as_view()), name='Add_doctor'),

    re_path(r'^doctor/udpate/(?P<pk>\d+)$', login_required(UpdateDoctor.as_view()), name = 'Update_doctor'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
