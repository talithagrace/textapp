from django.shortcuts import render
from django.http import HttpResponse
from twilio.rest import Client
from .models import SendSMS
from .forms import SendSMSForm
from .utils import send_twilio_message
from django.views.generic.edit import CreateView
from django.utils import timezone
from config import settings

def sendsms(request):
    if request.method == "POST":
        form = SendSMSForm(request.POST)
        if form.is_valid():
            number = form.cleaned_data['to_number']
            body = form.cleaned_data['body']
            sent = send_twilio_message(number, body)
            send_sms = form.save(commit=False)
            send_sms.from_number = settings.TWILIO_PHONE_NUMBER
            send_sms.sms_sid = sent.sid
            send_sms.account_sid = sent.account_sid
            send_sms.status = sent.status
            send_sms.sent_at = timezone.now()
            return render(request, 'smstwilio/sendsms_form.html', {'form':form})
    else:
        form = SendSMSForm()
    return render(request, 'smstwilio/sendsms_form.html', {'form':form})
