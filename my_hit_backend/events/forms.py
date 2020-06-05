from django import forms
from django.contrib.admin import widgets 
from .models import Event

 
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        labels = {
            "date": "Event date.",
        }
        widgets = {
            'date': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date', 'data-date-format': 'YYYY-MM-DD'}),
            'description': forms.Textarea(attrs={'rows': 4, },),
        }
        fields = ('image','name','date','description','location')
