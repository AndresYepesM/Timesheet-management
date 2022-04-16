from multiprocessing.sharedctypes import Value
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *


class NewUser(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'Username',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email address'
        }

class NewDoctor(forms.ModelForm):

    class Meta:
        model = Doctor
        fields = [
            'isDoctor',
            'ssn',
            'home_address',
            'phone_num',
            'specialty',
            'office_address',
            'isWest',
            'isEast',
        ]
        labels = {
            'isDoctor': 'Give the Doctor role.',
            'ssn': 'Social security number',
            'home_address': 'Personal address',
            'phone_num': 'Phone number',
            'specialty': 'Specialty',
            'office_address': 'Offices address',
            'isWest': 'is from the sector West?',
            'isEast': 'is from the sector East?'
        }


class UpdateUser(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'first_name',
            'last_name',
            'email',
            'is_active'
        ]

        labels = {
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Emaill address',
            'is_active': 'this user is still active?',
        }


class NewLocation(forms.ModelForm):
    class Meta:
        model = Location

        fields = [
            'name',
            'address',
            'isWest',
            'isEast'
        ]

        labels ={
            'name': 'Name of the facility',
            'address':'Address of the facility',
            'isWest': 'the facility is at sector West?',
            'isEast': 'the facility is at sector East?'
        }

class LocationUpdate(forms.ModelForm):
    class Meta:
        model = Location

        fields = [
            'name',
            'address',
            'isWest',
            'isEast',
            'isActive'
        ]

        labels ={
            'name': 'Name of the facility',
            'address':'Address of the facility',
            'isWest': 'the facility is at sector West?',
            'isEast': 'the facility is at sector East?',
            'isActive': 'This facility is still active?'
        }