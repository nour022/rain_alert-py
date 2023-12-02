from twilio.rest import Client

account_sid = 'ACdd903093f24fb6e28237856acde6f678'
auth_token = '8d5d5274d43684a4f626f178c3d66c0b'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+16205360296',
  body='Your Facebook code is 1238432\nhttps://www.facebook.com/',
  to='+4915758128078'
)

print(message.sid)