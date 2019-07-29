from django import forms
from learning_logs.models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields  = ['topic_text']
        labels = {
            'topic_text':''
        }

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields  = ['entry_text']
        labels = {
            'entry_text':''
        }
        widgets = {
            'entry_text':forms.Textarea(attrs = {'cols':80}) }

