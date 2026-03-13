import pandas as pd
import streamlit as st

st.title("📂 Page 1 — Upload CSV + exploration")

uploaded_file = st.file_uploader(
    "Choisir un fichier CSV",
    type=["csv"],
    help="Importez votre dataset. La dernière colonne sera utilisée comme cible sur la page d'entraînement."
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.session_state["df"] = df

    st.success("Dataset chargé avec succès.")

    col1, col2, col3 = st.columns(3)
    col1.metric("Lignes", df.shape[0])
    col2.metric("Colonnes", df.shape[1])
    col3.metric("Valeurs manquantes", int(df.isna().sum().sum()))

    tab1, tab2, tab3, tab4 = st.tabs(["Aperçu", "Types", "Statistiques", "Valeurs manquantes"])

    with tab1:
        st.dataframe(df.head(20), use_container_width=True)

    with tab2:
        types_df = pd.DataFrame(df.dtypes, columns=["Type"])
        st.dataframe(types_df, use_container_width=True)

    with tab3:
        st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

    with tab4:
        missing_df = df.isna().sum().reset_index()
        missing_df.columns = ["Colonne", "Nb_valeurs_manquantes"]
        st.dataframe(missing_df.sort_values("Nb_valeurs_manquantes", ascending=False), use_container_width=True)

    st.info("La page 2 utilisera automatiquement les colonnes numériques comme variables explicatives.")
else:
    st.warning("Importez un fichier CSV pour continuer.")
