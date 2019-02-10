# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
twilio_number = '+15017122661'

def send_text(content, dest):
    message = client.messages.create(
                              from_=twilio_number,
                              body=content,
                              to=dest
                          )

    print(message.sid)

def send_mms(content, img_url, dest):
    message = client.messages.create(
                              body=content,
                              from_=twilio_number,
                              media_url=twilio_number,
                              to=dest
                          )

    print(message.sid)

app = Flask(__name__)


@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message("Ahoy! Thanks so much for your message.")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
