# 📊 Dashboard de Predicción de Churn

Aplicación interactiva para predecir la fuga de clientes y estimar el impacto económico usando Machine Learning.

# 🚀 Descripción general

Este proyecto simula un escenario empresarial real donde una compañía necesita identificar clientes en riesgo de abandonar el servicio (churn) y tomar acciones proactivas.

El sistema combina:
- Un modelo de Machine Learning (Regresión Logística)
- Un dashboard orientado al negocio (Streamlit)
- Estimación del impacto económico para la toma de decisiones

# 🎯 Objetivos

- Predecir la probabilidad de fuga de cada cliente
- Clasificar clientes según su nivel de riesgo (Bajo / Medio / Alto)
- Estimar la pérdida potencial de ingresos
- Brindar recomendaciones accionables para el negocio

# 🧠 Modelo

- **Algoritmo:** Regresión Logística
- **Variable objetivo:** Churn (Sí / No)
- **Salida:** Probabilidad de fuga

**Variables utilizadas:**

- Antigüedad del cliente
- Cargo mensual
- Tipo de contrato
- Servicio de internet
- Método de pago
- Seguridad en línea
- Soporte técnico
- Facturación sin papel

# 💡 Lógica de negocio

Los clientes se clasifican en niveles de riesgo según su probabilidad de churn:

| Nivel de riesgo | Probabilidad | Estado |
|---|---|---|
| 🟢 Bajo | 0% – 30% | Estable |
| 🟡 Medio | 31% – 59% | En revisión |
| 🔴 Alto | 60% – 100% | Acción inmediata |


# 💰 Estimación del impacto económico

La aplicación estima la pérdida potencial de ingresos por cliente:
Impacto = Cargo mensual × Meses esperados × Probabilidad de churn
Los meses esperados se determinan según el tipo de contrato:

- **Mes a mes** → 3 meses
- **Contratos a largo plazo** → 12 meses

# 🖥️ Funcionalidades

- Simulación interactiva de clientes
- Predicción de churn en tiempo real
- Visualización de riesgo (sistema semáforo)
- Estimación del impacto económico
- Recomendaciones accionables para el negocio
- Explicabilidad del modelo (factores clave de fuga)

# 🛠️ Tecnologías utilizadas

![Python]
![Pandas]
![Scikit-learn]
![Streamlit]
![Joblib]

# 📂 Estructura del proyecto

├── app/
│   └── app.py               # Dashboard en Streamlit
├── train.py              # Entrenamiento del modelo
├── evaluate.py           # Evaluación del modelo
├── requirements.txt
│
├── data/
│   └── customers.csv
│
├── models/
│   ├── (se crearan una vez entrenado el modelo)
└── src/
    ├── preprocess.py
    └── __init__.py

# ⚙️ Instalación

git clone https://github.com/gianfrancomoscarella/churn-prediction-dashboard.git
cd churn-prediction-dashboard
pip install -r requirements.txt

# ▶️ Uso

**1. Entrenar el modelo**

python train.py

**2. Evaluar el modelo**

El script `evaluate.py` genera:
- Accuracy
- ROC AUC Score
- Matriz de confusión

**3. Ejecutar la aplicación**

python -m streamlit run app/app.py   

# ⚠️ Limitaciones

- Utiliza un dataset público (no datos reales de una empresa)
- No considera factores externos (condiciones de mercado, competencia)
- Las predicciones son probabilísticas, no determinísticas

# 👤 Autor

**Gianfranco Moscarella**  
 
[LinkedIn](https://linkedin.com/in/gianfranco-moscarella)
