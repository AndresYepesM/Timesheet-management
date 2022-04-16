from django import forms
from workday.models import *

class TimeInput(forms.TimeInput):
    input_type ='time'

class ClockInOut(forms.ModelForm):
    class Meta:
        model = Timecard

        widgets={
            'clock_in': TimeInput(), 

            'clock_out':TimeInput(),
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