import streamlit as st

st.set_page_config(page_title="Conversor de Temperatura", page_icon="🌡️")

st.title("🌡️ Conversor de Temperatura")
st.write("Convierte unidades de temperatura de forma rápida y sencilla.")

CERO_ABSOLUTO_C = -273.15

def celsius_a_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_a_kelvin(c):
    return c + 273.15

def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9

def kelvin_a_celsius(k):
    return k - 273.15

col1, col2 = st.columns(2)

with col1:
    valor_origen = st.number_input("Ingresa el valor:", value=0.0, step=1.0, format="%.2f")

with col2:
    escala_origen = st.selectbox(
        "Escala de origen:",
        ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    )
es_valido = True
temp_celsius = 0.0

if escala_origen == "Celsius (°C)":
    temp_celsius = valor_origen
elif escala_origen == "Fahrenheit (°F)":
    temp_celsius = fahrenheit_a_celsius(valor_origen)
elif escala_origen == "Kelvin (K)":
    temp_celsius = kelvin_a_celsius(valor_origen)

if temp_celsius < CERO_ABSOLUTO_C:
    st.error(f"Error: La temperatura ingresada está por debajo del cero absoluto ({CERO_ABSOLUTO_C} °C). Físicamente imposible.")
    es_valido = False

if es_valido:
    st.subheader("Resultados de la Conversión:")
    
    c_final = temp_celsius
    f_final = celsius_a_fahrenheit(temp_celsius)
    k_final = celsius_a_kelvin(temp_celsius)
    
    res_col1, res_col2, res_col3 = st.columns(3)
    
    with res_col1:
        st.metric(label="Celsius", value=f"{c_final:.2f} °C")
    with res_col2:
        st.metric(label="Fahrenheit", value=f"{f_final:.2f} °F")
    with res_col3:
        st.metric(label="Kelvin", value=f"{k_final:.2f} K")
