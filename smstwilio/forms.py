from .models import SendSMS
from django import forms

class SendSMSForm(forms.ModelForm):

    class Meta:
        model = SendSMS
        fields = ('to_number', 'body',)
