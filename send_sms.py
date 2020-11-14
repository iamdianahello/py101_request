import os

from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
NUMBER_FROM = os.getenv('NUMBER_FROM')
NUMBER_TO = os.getenv('NUMBER_TO')


def send_panic_msg():
    client.messages.create(
        body='ALARM SERVER FAIL',  # текст сообщения
        from_=NUMBER_FROM,  # номер, который был получен
        to=NUMBER_TO,  # твой номер, на который придёт sms
        )

