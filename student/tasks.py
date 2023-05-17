import os

from celery import shared_task
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
verify_sid = os.environ['TWILIO_VERIFY_SID']
trial_number = os.environ['TWILIO_TRIAL_NUMBER']

@shared_task
def send_sms(first_name, number):
    message = client.messages.create(
        body=f'{first_name}, you have been registered',
        from_=trial_number,
        to=number
    )
    print(message.sid)
