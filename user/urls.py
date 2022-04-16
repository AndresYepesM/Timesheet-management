from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from user.views import *

urlpatterns = [

    # Doctors urls

    path('main/', AdministrationMainPage, name='Admin_main_page'),

    path('doctors/main', login_required(DoctorsList.as_view()), name='Doctor_list'),
    
    re_path(r'^doctor/detail/(?P<pk>\d+)$',login_required(DoctorDetail.as_view()), name='Doctor_detail'),

    path('doctor/create',login_required(CreateNewDoctor.as_view()), name='Add_doctor'),

    re_path(r'^doctor/udpate/(?P<pk>\d+)$',login_required(UpdateDoctor.as_view()), name='Update_doctor'),


    # Location urls
    # Location list works for both roles admin and doctor
    path('doctors/location_availables', login_required(LocationList.as_view()), name='Location_list'),

    path('location/create', login_required(LocatioCreate.as_view()), name='Location_create'),

     re_path(r'^location/update/(?P<pk>\d+)$',login_required(UpdateLocation.as_view()), name='Location_update'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
