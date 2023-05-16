import os

from celery import shared_task
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)
verify_sid = os.environ['TWILIO_VERIFY_SID']
verified_number = "+380661260865"


@shared_task
def send_sms(number):
    verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=number, channel="sms")
    print(verification.status)
