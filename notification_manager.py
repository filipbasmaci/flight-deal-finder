from twilio.rest import Client

TWILIO_SID = "your twilio sid here"
TWILIO_AUTH_TOKEN = "your twilio auth here"
TWILIO_VIRTUAL_NUMBER = "your twilio virtual here"
TWILIO_VERIFIED_NUMBER = "your twilio verified number here"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)