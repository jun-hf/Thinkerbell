from django import forms 
from .models import Log, Entry

class LogForm(forms.ModelForm):
    class Meta:
        model = Log
        fields = ['content']
        labels = {'content': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['content']
        labels = {'content': 'Entry'}
        widgets = {'content': forms.Textarea(attrs={'cols': 80})}