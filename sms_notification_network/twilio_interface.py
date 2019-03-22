# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse



app = Flask(__name__)


def send_text(content, dest):
    content += " Reply STOP to stop SMS notifications."
    message = client.messages.create(
                              from_=twilio_number,
                              body=content,
                              to=dest
                          )

    print(message.sid)

def send_mms(content, img_url, dest):
    content += " Reply STOP to stop SMS notifications."
    message = client.messages.create(
                              body=content,
                              from_=twilio_number,
                              media_url=twilio_number,
                              to=dest
                          )

    print(message.sid)

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    """Respond to incoming messages with a friendly SMS."""
    # Get information about the
    number = request.form['From']
    message_body = request.form['Body']

    if message_body == "STOP":
        # do action to stop sms notifications for user
        text = "You have unsubscribed from SMS notifications."
    else:
        text = "Invalid Response. Reply STOP to stop SMS notifications."


    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(text)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
