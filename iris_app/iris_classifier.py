import pandas as pd
import plotly.express as px
import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="centered")

st.title("🌸 Application de classification Iris")
st.write("Prédiction de l'espèce d'une fleur à partir de ses caractéristiques.")

@st.cache_data
def load_iris_data():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    return iris, X, y

iris, X, y = load_iris_data()

@st.cache_resource
def train_model(X, y):
    model = RandomForestClassifier(random_state=42)
    model.fit(X, y)
    return model

model = train_model(X, y)
class_names = iris.target_names

st.subheader("Choisissez les valeurs des 4 features")

col1, col2 = st.columns(2)

with col1:
    sepal_length = st.slider(
        "Sepal length (cm)",
        min_value=float(X.iloc[:, 0].min()),
        max_value=float(X.iloc[:, 0].max()),
        value=5.4,
        help="Longueur du sépale en centimètres.",
    )
    sepal_width = st.slider(
        "Sepal width (cm)",
        min_value=float(X.iloc[:, 1].min()),
        max_value=float(X.iloc[:, 1].max()),
        value=3.4,
        help="Largeur du sépale en centimètres.",
    )

with col2:
    petal_length = st.slider(
        "Petal length (cm)",
        min_value=float(X.iloc[:, 2].min()),
        max_value=float(X.iloc[:, 2].max()),
        value=1.3,
        help="Longueur du pétale en centimètres.",
    )
    petal_width = st.slider(
        "Petal width (cm)",
        min_value=float(X.iloc[:, 3].min()),
        max_value=float(X.iloc[:, 3].max()),
        value=0.2,
        help="Largeur du pétale en centimètres.",
    )

input_df = pd.DataFrame([{
    iris.feature_names[0]: sepal_length,
    iris.feature_names[1]: sepal_width,
    iris.feature_names[2]: petal_length,
    iris.feature_names[3]: petal_width
}])

st.write("### Valeurs saisies")
st.dataframe(input_df, use_container_width=True)

if st.button("Prédire", use_container_width=True):
    prediction = model.predict(input_df)[0]
    probabilities = model.predict_proba(input_df)[0]

    st.success(f"Espèce prédite : **{class_names[prediction]}**")

    prob_df = pd.DataFrame({
        "Espèce": class_names,
        "Probabilité": probabilities
    })

    fig = px.bar(
        prob_df,
        x="Espèce",
        y="Probabilité",
        text="Probabilité",
        title="Probabilités par classe",
        labels={"Probabilité": "Probabilité", "Espèce": "Classe"},
    )
    fig.update_traces(texttemplate="%{text:.2f}", textposition="outside")
    fig.update_layout(yaxis_range=[0, 1])
    st.plotly_chart(fig, use_container_width=True)

st.caption("TP Streamlit - Exercice 1")
