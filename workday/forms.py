from django import forms
from workday.models import *
from user.models import *
from django.contrib.auth.models import User

class TimeInput(forms.TimeInput):
    input_type ='time'

class ClockIn(forms.ModelForm):
    
    class Meta:
        model = Timecard

        widgets={
            'clock_in': TimeInput(),
            'slug': forms.NumberInput(attrs={'readonly':'readonly'})
        }

        fields = [
            'slug',
            'clock_in',
            'zone',
        ]

        labels = {
            'clock_in': 'Click to clock in',
            'zone': 'which zone is',
            'slug':' '
        }


class ClockOut(forms.ModelForm):
    
    class Meta:
        model = Timecard

        widgets = {
            'clock_out': TimeInput(),
            'clock_in':forms.TimeInput(attrs={'readonly':'readonly'})
        }

        fields = [
            'clock_in',
            'clock_out',
        ]

        labels = {
            'clock_out': 'Click to clock out',
            'clock_in': 'Your clock in time',
        }