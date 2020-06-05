from django import forms
from django.contrib.admin import widgets 
from .models import Accomodation

 
class AccomodationForm(forms.ModelForm):
    class Meta:
        model = Accomodation
        labels = {
            "available_spaces": "Enter number of available spaces.",

        }
        fields = ('name','price','available_spaces')

