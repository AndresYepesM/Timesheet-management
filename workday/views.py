from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from workday.models import Timecard
from workday.forms import *
from user.models import Doctor, Location, Sector

# Create your views here.

@login_required(login_url='/accounts/login')
def TodayActivity(request, pk):
    cu = request.user.doctor
    current_date = date.today()
    context = {
        'employee': Doctor.objects.get(user_id=pk),
        'timecard': Timecard.objects.filter(employee=cu, workday=current_date),
        'today': date.today()
    }
    return render(request, 'timesheet/activity.html', context)


class ClockInMethod(CreateView):
    model = Timecard
    second_model = Location
    form_class = ClockIn
    template_name = 'timesheet/clock_in_out.html'
    success_url = reverse_lazy('Admin_main_page')
    
    def get_context_data(self, **kargs):
        context = super(ClockInMethod, self).get_context_data(**kargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context
    
    def get_form(self, *args, **kwargs):
        form = super(ClockInMethod, self).get_form(*args, **kwargs)
        if form.is_bound == False:
            current_zone = self.request.user.doctor.sector
            locations =  self.second_model.objects.filter(sector = current_zone, isActive=True)
            form.fields['zone'].queryset = locations
        return form

    def post(self, request, *args, **kwargs):
        self.object=self.get_object
        current_user = self.request.user.doctor

        form = self.form_class(request.POST)

        if form.is_valid():
            form.instance.employee = current_user
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class ClockOutMethod(UpdateView):
    model = Timecard
    second_model = Location
    form_class = ClockOut
    template_name = 'timesheet/clock_in_out.html'
    success_url = reverse_lazy('Admin_main_page')

