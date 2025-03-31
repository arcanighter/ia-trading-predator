import requests
from requests.auth import HTTPBasicAuth

def send_whatsapp_message(message):
    account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth_token = 'your_auth_token'
    from_number = 'whatsapp:+14155238886'
    to_number = 'whatsapp:+336XXXXXXXX'

    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        'From': from_number,
        'To': to_number,
        'Body': message
    }

    try:
        response = requests.post(url, data=data, auth=HTTPBasicAuth(account_sid, auth_token))
        if response.status_code == 201:
            print("Message WhatsApp envoyé.")
        else:
            print(f"Erreur WhatsApp : {response.text}")
    except Exception as e:
        print(f"Erreur d'envoi WhatsApp : {e}")
