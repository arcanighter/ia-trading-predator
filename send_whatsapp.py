import requests
from requests.auth import HTTPBasicAuth

def send_whatsapp_message(message):
    account_sid = 'ACf7b5aa9c7f06f967c4ee46c3fb33ce7d'
    auth_token = 'eac0fdb4b20da20f7827d4a44a0c11a9'
    from_number = 'whatsapp:+14155238886'
    to_number = 'whatsapp:+33678425289'

    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        'From': from_number,
        'To': to_number,
        'Body': message
    }

    try:
        response = requests.post(url, data=data, auth=HTTPBasicAuth(account_sid, auth_token))
        if response.status_code == 201:
            print("✅ Message WhatsApp envoyé avec succès.")
        else:
            print(f"❌ Erreur WhatsApp : {response.status_code} – {response.text}")
    except Exception as e:
        print(f"❌ Exception lors de l'envoi WhatsApp : {e}")
