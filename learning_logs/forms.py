from django import forms
from django.forms import fields, widgets

from .models import Entry, Topic

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text' : ''}
    
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = {'text'}
        labels = {'text': ''}
        widgets = {'text': forms.Textarea(attrs={'clos':80})}