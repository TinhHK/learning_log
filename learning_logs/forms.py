from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['name']
		labels = {'name': ''}

class EntryForm(forms.ModelForm):
	class Meta:
		model = Entry
		fields = ['description']
		labels = {'description': ''}
		widgets = {'description':forms.Textarea(attrs={'cols':80})}