import pandas as pd
import streamlit as st

st.title("🔮 Page 3 — Interface de prédiction")

if "model" not in st.session_state or "feature_cols" not in st.session_state:
    st.warning("Aucun modèle disponible. Passez d'abord par la page 2_Training.")
else:
    model = st.session_state["model"]
    feature_cols = st.session_state["feature_cols"]
    feature_defaults = st.session_state.get("feature_defaults", {})
    target_col = st.session_state.get("target_col", "prédiction")

    st.write("Saisissez les valeurs des variables pour obtenir une prédiction.")

    display_cols = feature_cols[:12]
    col1, col2 = st.columns(2)
    user_input = {}

    for i, col in enumerate(display_cols):
        default_value = float(feature_defaults.get(col, 0.0))
        if i % 2 == 0:
            with col1:
                user_input[col] = st.number_input(
                    col,
                    value=default_value,
                    help=f"Valeur de la variable {col}."
                )
        else:
            with col2:
                user_input[col] = st.number_input(
                    col,
                    value=default_value,
                    help=f"Valeur de la variable {col}."
                )

    for col in feature_cols:
        if col not in user_input:
            user_input[col] = float(feature_defaults.get(col, 0.0))

    input_df = pd.DataFrame([user_input])[feature_cols]

    st.write("### Données de prédiction")
    st.dataframe(input_df[display_cols], use_container_width=True)

    if st.button("Prédire", use_container_width=True):
        prediction = model.predict(input_df)[0]
        st.success(f"Valeur prédite pour **{target_col}** : **{prediction:,.2f}**")
