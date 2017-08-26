from django.conf.urls import url
from . import sms_views

urlpatterns = [
    url(r'^sms/$', sms_views.sendsms, name='sms'),
]
