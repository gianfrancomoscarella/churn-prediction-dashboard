import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Churn Dashboard", layout="wide")

# HEADER

st.markdown("""
### Análisis predictivo para abandono de clientes""")

# LOAD

modelo = joblib.load("models/modelo.pkl")
columnas = joblib.load("models/columnas.pkl")
escalador = joblib.load("models/escalador.pkl")

# MAPAS

mapa_contrato = {
    "Mensual": "Month-to-month",
    "1 año": "One year",
    "2 años": "Two year"
}

mapa_internet = {
    "ADSL": "DSL",
    "Fibra": "Fiber optic",
    "Sin servicio": "No"
}

mapa_pago = {
    "Pago electrónico": "Electronic check",
    "Cheque": "Mailed check",
    "Transferencia": "Bank transfer (automatic)",
    "Tarjeta": "Credit card (automatic)"
}

mapa_si_no = {"Sí": "Yes", "No": "No"}

# SIDEBAR

st.sidebar.header("🧾 Perfil del cliente")

antiguedad = st.sidebar.slider("Antigüedad (meses)", 0, 72, 12)
gasto = st.sidebar.number_input("Gasto mensual", 10.0, 200.0, 50.0)

contrato_ui = st.sidebar.selectbox("Contrato", list(mapa_contrato.keys()))
internet_ui = st.sidebar.selectbox("Internet", list(mapa_internet.keys()))
pago_ui = st.sidebar.selectbox("Forma de pago", list(mapa_pago.keys()))

seguridad_ui = st.sidebar.selectbox("Seguridad online", list(mapa_si_no.keys()))
soporte_ui = st.sidebar.selectbox("Soporte técnico", list(mapa_si_no.keys()))
factura_ui = st.sidebar.selectbox("Factura electrónica", list(mapa_si_no.keys()))

# MAPEO

contrato = mapa_contrato[contrato_ui]
internet = mapa_internet[internet_ui]
pago = mapa_pago[pago_ui]
seguridad = mapa_si_no[seguridad_ui]
soporte = mapa_si_no[soporte_ui]
factura = mapa_si_no[factura_ui]

# DATA

datos = pd.DataFrame(columns=columnas)
datos.loc[0] = 0

datos["tenure"] = antiguedad
datos["MonthlyCharges"] = gasto

datos[["tenure", "MonthlyCharges"]] = escalador.transform(
    datos[["tenure", "MonthlyCharges"]]
)

def activar(col):
    if col in columnas:
        datos[col] = 1

activar(f"Contract_{contrato}")
activar(f"InternetService_{internet}")
activar(f"PaymentMethod_{pago}")
activar(f"OnlineSecurity_{seguridad}")
activar(f"TechSupport_{soporte}")
activar(f"PaperlessBilling_{factura}")

datos = datos[columnas]

# BOTÓN

if st.sidebar.button("🔍 Analizar cliente"):

    proba = modelo.predict_proba(datos)[0][1]
    porcentaje = proba * 100

    
    # KPI CARDS
    
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Probabilidad de abandono", f"{porcentaje:.2f}%")

    with col2:
        st.metric("Antigüedad", f"{antiguedad} meses")

    with col3:
        st.metric("Ingreso mensual", f"${gasto:.0f}")

    st.progress(int(porcentaje))

    
    # SEMÁFORO
    
    if porcentaje >= 60:
        st.error("🔴 Alto riesgo de abandono")
        nivel = "Alto"
    elif porcentaje >= 31:
        st.warning("🟡 Cliente en revisión")
        nivel = "Medio"
    else:
        st.success("🟢 Cliente estable")
        nivel = "Bajo"

    
    # DETALLE
    
    st.markdown("---")
    st.subheader("📌 Análisis del cliente")

    colA, colB = st.columns(2)

    with colA:
        st.write(f"• Tipo de contrato: {contrato_ui}")
        st.write(f"• Servicio de internet: {internet_ui}")
        st.write(f"• Método de pago: {pago_ui}")

    with colB:
        st.write(f"• Seguridad online: {seguridad_ui}")
        st.write(f"• Soporte técnico: {soporte_ui}")
        st.write(f"• Facturación electrónica: {factura_ui}")

    
    # IMPACTO ECONÓMICO
    
    st.markdown("---")
    st.subheader("Impacto económico estimado")

    if contrato == "Month-to-month":
        meses = 3
    else:
        meses = 12

    impacto = gasto * meses * proba

    st.metric("Ingreso en riesgo", f"${impacto:.0f}")

    # RECOMENDACIÓN
    
    st.markdown("---")
    st.subheader("Recomendación")

    if nivel == "Alto":
        st.write("• Contactar cliente de forma inmediata")
        st.write("• Ofrecer descuento o beneficio")
        st.write("• Incentivar contrato a largo plazo")

    elif nivel == "Medio":
        st.write("• Realizar seguimiento")
        st.write("• Ofrecer mejoras en servicio")
        st.write("• Evaluar retención preventiva")

    else:
        st.write("• Mantener condiciones actuales")
        st.write("• Cliente estable")
    
st.caption("Estimación basada en modelo estadístico. No representa certeza absoluta.")  