from django import forms
from .models import Events, Comment


class EventForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('public', 'title','start_date', 'end_date', 'location', 'text')

    def clean_text(self):
        text  = self.cleaned_data.get('text')
        badwords = ['fuck']
        check_list = [True if w in text else False for w in badwords]
        # if title exists create slug from title
        if True in check_list:
            for word in badwords:
                text = text.replace(word, '*' * len(word))

        return text

    def clean(self):
        start_date = self.cleaned_data.get("start_date")
        end_date = self.cleaned_data.get("end_date")
        if end_date < start_date:
            msg = "End date should be greater than start date."
            self._errors["end_date"] = self.error_class([msg])

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            "text": "Type Comment"
        }
