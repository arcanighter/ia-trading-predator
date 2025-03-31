import streamlit as st
from modules.predictor import predict
from send_whatsapp import send_whatsapp_message

st.title("🤖 IA Trading V1")

asset = st.text_input("🔍 Entrez un actif (ex : BTC, AAPL, EURUSD)")

if st.button("Lancer la prédiction"):
    if asset:
        prediction = predict(asset)
        st.success(f"📈 Prédiction pour {asset} : {prediction}")
        send_whatsapp_message(f"📲 Prédiction IA pour {asset} : {prediction}")
    else:
        st.warning("Veuillez entrer un actif.")
