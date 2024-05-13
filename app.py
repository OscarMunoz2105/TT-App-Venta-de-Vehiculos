import pandas as pd
import plotly.express as px
import streamlit as st

# Leer el archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# Agregar un encabezado
st.header('Análisis de datos de anuncios de venta de coches')

# Crear una casilla de verificación para construir un histograma
build_histogram = st.checkbox('Construir un histograma')

# Crear una casilla de verificación para construir un gráfico de dispersión
build_scatter = st.checkbox('Construir un gráfico de dispersión')

if build_histogram: # si la casilla de verificación de histograma está marcada
    st.write('Construyendo un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

if build_scatter: # si la casilla de verificación de gráfico de dispersión está marcada
    st.write('Construyendo un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    fig = px.scatter(car_data, x="model_year", y="price")  # Corrección aquí: "model_year" en lugar de "year"
    st.plotly_chart(fig, use_container_width=True)
