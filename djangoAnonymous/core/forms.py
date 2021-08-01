from django import forms
from django import forms
from .models import Message


# crreate a frm for the messages
class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ("message",)
