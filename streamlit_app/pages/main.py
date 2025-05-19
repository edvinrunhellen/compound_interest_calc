import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt

# Ladda in datan med rätt avgränsare
@st.cache_data
def load_data():
    return pd.read_csv("car_price_dataset.csv", delimiter=";")

# Hämta datan
df = load_data()

st.title("🚗 Bilpris-analys & prediktion")

# Visa data
st.subheader("Dataview")
st.dataframe(df)

# Kolumner att välja som input/output
numeric_columns = df.select_dtypes(include=np.number).columns.tolist()

if len(numeric_columns) < 2:
    st.warning("Datasetet behöver minst två numeriska kolumner.")
else:
    x_col = st.selectbox("Välj X (oberoende variabel)", numeric_columns, index=0)
    y_col = st.selectbox("Välj Y (beroende variabel)", numeric_columns, index=1)

    # Skapa modell
    X = df[[x_col]].values
    y = df[y_col].values
    model = LinearRegression()
    model.fit(X, y)

    # Prediktion
    st.subheader("🔮 Gör en prediktion")
    input_val = st.number_input(f"Ange värde för {x_col}:", value=float(X.mean()))
    prediction = model.predict([[input_val]])
    st.write(f"Förväntat värde på {y_col}: **{prediction[0]:,.2f}**")

    # Visa graf
    st.subheader("📈 Regression plot")
    fig, ax = plt.subplots()
    ax.scatter(X, y, color='blue', label='Data')
    ax.plot(X, model.predict(X), color='red', label='Lin. regression')
    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)
    ax.legend()
    st.pyplot(fig)

