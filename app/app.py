import streamlit as st

import streamlit as st

password = st.text_input("Mot de passe", type="password")

if password != "tp3_mbg":
    st.warning("Mot de passe incorrect")
    st.stop()

st.set_page_config(page_title="TP1 ML Multi-Pages", page_icon="🏠", layout="wide")

st.title("🏠 Application ML Multi-Pages")
st.write(
    '''
    Bienvenue dans l'application multi-pages pour le dataset TP1.

    Utilisez le menu latéral pour naviguer entre :
    - **1_Data** : chargement et exploration du CSV
    - **2_Training** : entraînement du modèle et visualisation des performances
    - **3_Prediction** : interface de prédiction
    '''
)

st.info("Commencez par la page **1_Data** pour importer votre fichier CSV.")
