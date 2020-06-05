from django import forms
from .models import Timetable

 
class TimetabeForm(forms.ModelForm):
    class Meta:
        model = Timetable
        labels = {
            "file_name": "Upload PDF Timetable.",
            "course": "Select Course.",
        }

        fields = ('course','file_name')

