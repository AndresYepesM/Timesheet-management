from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from workday.models import *
from workday.forms import *

# Create your views here.


@login_required(login_url='/accounts/login')
def Timecard_mainpage(request):
    return render(request, 'timesheet/user_timecard.html')



class NewWorkday(CreateView):
    model = Timecard
    form_class = ClockInOut
    template_name = 'timesheet/clock_in_out.html'