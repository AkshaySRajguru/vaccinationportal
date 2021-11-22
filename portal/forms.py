from django import forms
from .models import *
from django.forms import fields


class PersonForm(forms.ModelForm):
    dob = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    dov = fields.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Person
        fields = '__all__'
