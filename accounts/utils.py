from twilio.rest import Client


account_sid = "..."
auth_token = "..."

client = Client(account_sid, auth_token)


def send_sms(user_code, phone_number):
    message = client.messages.create(
        body=f'Hi! Your user and verification code: {user_code}',
        from_='...',
        to=f'{phone_number}'
    )
    print(message.sid)
