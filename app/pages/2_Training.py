import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

st.title("🧠 Page 2 — Entraînement du modèle + performances")

if "df" not in st.session_state:
    st.warning("Aucun dataset chargé. Allez d'abord sur la page 1_Data.")
else:
    df = st.session_state["df"].copy()

    target_default = "SalePrice" if "SalePrice" in df.columns else df.columns[-1]
    target_col = st.selectbox(
        "Choisissez la variable cible",
        options=df.columns.tolist(),
        index=df.columns.tolist().index(target_default),
        help="Pour le dataset House Prices, choisissez SalePrice."
    )

    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    feature_cols = [c for c in numeric_cols if c != target_col]

    if len(feature_cols) == 0:
        st.error("Aucune feature numérique exploitable n'a été trouvée.")
    else:
        X = df[feature_cols].copy()
        y = pd.to_numeric(df[target_col], errors="coerce")

        valid_mask = y.notna()
        X = X.loc[valid_mask].copy()
        y = y.loc[valid_mask].copy()

        X = X.fillna(X.median(numeric_only=True))

        col1, col2 = st.columns(2)
        with col1:
            test_size = st.slider(
                "Taille du jeu de test",
                min_value=0.1, max_value=0.4, value=0.2, step=0.05,
                help="Part des données réservée à l'évaluation."
            )
        with col2:
            n_estimators = st.slider(
                "Nombre d'arbres (Random Forest)",
                min_value=50, max_value=500, value=200, step=50,
                help="Plus il y a d'arbres, plus le modèle peut être stable, mais plus l'entraînement est long."
            )

        st.write(f"**Cible choisie :** `{target_col}`")
        st.write(f"**Nombre de variables numériques utilisées :** {len(feature_cols)}")

        if st.button("Entraîner le modèle", use_container_width=True):
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42
            )

            model = RandomForestRegressor(
                n_estimators=n_estimators,
                random_state=42
            )
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)

            mae = mean_absolute_error(y_test, y_pred)
            rmse = np.sqrt(mean_squared_error(y_test, y_pred))
            r2 = r2_score(y_test, y_pred)

            st.session_state["model"] = model
            st.session_state["feature_cols"] = feature_cols
            st.session_state["feature_defaults"] = X.median(numeric_only=True).to_dict()
            st.session_state["target_col"] = target_col

            m1, m2, m3 = st.columns(3)
            m1.metric("MAE", f"{mae:,.2f}")
            m2.metric("RMSE", f"{rmse:,.2f}")
            m3.metric("R²", f"{r2:.4f}")

            result_df = pd.DataFrame({
                "Valeur réelle": y_test,
                "Valeur prédite": y_pred
            })

            fig1 = px.scatter(
                result_df,
                x="Valeur réelle",
                y="Valeur prédite",
                title="Valeurs réelles vs valeurs prédites"
            )
            st.plotly_chart(fig1, use_container_width=True)

            importance_df = pd.DataFrame({
                "Feature": feature_cols,
                "Importance": model.feature_importances_
            }).sort_values("Importance", ascending=False).head(15)

            fig2 = px.bar(
                importance_df,
                x="Importance",
                y="Feature",
                orientation="h",
                title="Top 15 des variables les plus importantes"
            )
            st.plotly_chart(fig2, use_container_width=True)
