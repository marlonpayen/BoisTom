'''
Created on 28 Jun 2024

@author: mpayen
'''

from django import forms
from website.models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("nom", "email", "sujet", "message")
        
    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)
        self.fields['nom'].required = True
        self.fields['email'].required = True
        self.fields['sujet'].required = False
        self.fields['message'].required = True