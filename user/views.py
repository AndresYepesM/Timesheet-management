from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.template import loader
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from user.models import *
from user.forms import *

# Create your views here.


@login_required(login_url='/accounts/login')
# Administration main page
def AdministrationMainPage(request):
    return render(request, 'administration/main_admin_page.html')


class DoctorsList(ListView):
    model = Doctor
    template_name = 'administration/doctors/doctors_list.html'
    context_object_name = 'doctors'


class LocationList(ListView):
    model = Location
    template_name = 'administration/doctors/locations_list.html'
    context_object_name = 'locations'


class DoctorDetail(DetailView):
    model = Doctor
    template_name = 'administration/doctors/doctor_detail.html'


class CreateNewDoctor(CreateView):
    model = Doctor
    template_name = 'administration/doctors/new_doctor.html'
    form_class = NewUser
    second_form_class = NewDoctor
    success_url = reverse_lazy('Doctor_list')

    def get_context_data(self, **kargs):
        context = super(CreateNewDoctor, self).get_context_data(**kargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            auth_user = form.save()
            form2.instance.user = auth_user
            form2.save()
            auth_user.save()

            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))


class UpdateDoctor(UpdateView):
    model = User
    second_model = Doctor
    template_name = 'administration/doctors/new_doctor.html'
    form_class = UpdateUser
    second_form_class = NewDoctor
    success_url = reverse_lazy('Doctor_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateDoctor, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk', 0)
        user = self.model.objects.get(id=pk)
        doctor = self.second_model.objects.get(ssn=user.doctor.ssn)
        if 'form' not in context:
            context['form'] = self.form_class
        if 'form2' not in context:
            context['form2'] = self.second_form_class(instance=doctor)
        context['id'] = pk
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        id_user = kwargs['pk']
        user = self.model.objects.get(id=id_user)
        doctor = self.second_model.objects.get(ssn=user.doctor.ssn)
        form = self.form_class(request.POST, instance=user)
        form2 = self.second_form_class(request.POST, instance=doctor)
        if form.is_valid() and form2.is_valid():
            form.save()
            form2.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return HttpResponseRedirect(self.get_success_url())
