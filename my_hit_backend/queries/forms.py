from django import forms
from django.contrib.admin import widgets 
from .models import Comment,Query

 
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        labels = {
            "reply_message": "Enter your reply here.",

        }
        widgets ={
            'query': forms.TextInput(attrs={'type':'hidden',},),
            'commentator': forms.TextInput(attrs={'type':'hidden',},),
            'reply_message': forms.Textarea(attrs={'rows':3,},),
        }
        fields = ('query','commentator','reply_message')

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ('department','student','title','query_description')
