from django import forms
from .models import Events, Comment


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('public', 'title', 'text')



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Type Comment"
        }
