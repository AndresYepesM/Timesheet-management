from django import forms
from workday.models import *
from user.models import *
from django.contrib.auth.models import User

class TimeInput(forms.TimeInput):
    input_type ='time'

class ClockInOut(forms.ModelForm):
    class Meta:
        model = Timecard

        widgets={
            'clock_in': TimeInput(), 

            'clock_out':TimeInput(),

            'employee':forms.TextInput(attrs={'readonly':'readonly'})
        }

        fields = [
            'clock_in',
            'clock_out',
            'employee',
            'zone',
        ]

        labels = {
            'clock_in': 'Click to clock in',
            'clocl_out': 'Click to clock out',
            'employee': 'select you account',
            'zone': 'which zone is',
        }
    