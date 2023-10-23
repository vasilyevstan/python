import os
import credentials as cred
from twilio.rest import Client


client = Client(cred.account_sid, cred.auth_token)

message = client.messages.create(
                              from_ = "whatsapp:+14155238886",
                              body = 'Hello world!',
                              to = cred.receiver
                          )

print(message.sid)
