from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]
        labels = {'content': ''}
        widgets = {'content': forms.Textarea(attrs={'rows': 3})}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) # Get the user from kwargs
        super(MessageForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(MessageForm, self).save(commit=False)
        if self.user:
            instance.user = self.user
        if commit:
            instance.save()
        return instance
