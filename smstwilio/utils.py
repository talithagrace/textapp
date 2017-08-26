from config import settings
import twilio
from twilio.rest import Client

def send_twilio_message(to_number, body):
    client = twilio.rest.Client(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    return client.messages.create(
        body=body,
        to=to_number,
        from_=settings.TWILIO_PHONE_NUMBER,
    )
