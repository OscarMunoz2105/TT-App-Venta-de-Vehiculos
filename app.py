import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Crear un botón para construir un histograma
hist_button = st.button('Construir histograma')

# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if hist_button: # si se hace clic en el botón de histograma
    st.write('Construyendo un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if scatter_button: # si se hace clic en el botón de gráfico de dispersión
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="model_year", y="price")  # Corrección aquí: "model_year" en lugar de "year"
    st.plotly_chart(fig, use_container_width=True)