import requests
import streamlit as st
from requests.auth import HTTPBasicAuth

def send_whatsapp_message(message):
    account_sid = st.secrets["TWILIO_ACCOUNT_SID"]
    auth_token = st.secrets["TWILIO_AUTH_TOKEN"]
    from_number = st.secrets["TWILIO_FROM"]
    to_number = st.secrets["TWILIO_TO"]

    url = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
    data = {
        'From': from_number,
        'To': to_number,
        'Body': message
    }

    try:
        response = requests.post(url, data=data, auth=HTTPBasicAuth(account_sid, auth_token))

        # ✅ Affiche la réponse directement dans Streamlit
        st.write("📡 Code retour Twilio :", response.status_code)
        st.write("📨 Réponse complète :", response.text)

        if response.status_code == 201:
            st.success("✅ Message WhatsApp envoyé avec succès.")
        else:
            st.error("❌ Échec de l'envoi du message WhatsApp.")
    except Exception as e:
        st.error(f"❌ Erreur d'envoi WhatsApp : {e}")
