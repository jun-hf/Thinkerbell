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
        feilds = ['text']
        labels = {'text': 'Entry'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}