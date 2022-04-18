from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from workday.models import *
from workday.forms import *
from user.models import *

# Create your views here.


@login_required(login_url='/accounts/login')
def Timecard_mainpage(request):

    return render(request, 'timesheet/user_timecard.html')


class NewWorkday(CreateView):
    model = Timecard
    second_model = Doctor
    form_class = ClockInOut
    template_name = 'timesheet/clock_in_out.html'
    success_url = reverse_lazy('Timecard_main')
    

    def get_context_data(self, **kargs):

        context = super(NewWorkday, self).get_context_data(**kargs)
        current_user = self.request.user
        print(current_user)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):

        self.object=self.get_object
        form = self.form_class(request.POST)
        
        if form.is_valid():
            form.instance.employee == self.current_user.username
            form.save()

            return HttpResponseRedirect(self.get_success_url())
