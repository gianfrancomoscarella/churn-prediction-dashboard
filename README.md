📊 Customer Churn Prediction

Proyecto de análisis de datos y Machine Learning enfocado en la predicción de abandono de clientes (churn).

🚀 Objetivo

Desarrollar un modelo capaz de identificar clientes con alta probabilidad de abandono, utilizando variables como tipo de contrato, antigüedad y costo mensual.

🧠 Enfoque técnico
Limpieza y preprocesamiento de datos con Pandas
Transformación de variables categóricas mediante One-Hot Encoding
Entrenamiento de modelo de clasificación (Regresión Logística)
Evaluación con métricas:
Accuracy
Precision / Recall
Confusion Matrix
📈 Resultados

El modelo logra predecir correctamente patrones de abandono, identificando variables relevantes como:

Tipo de contrato
Antigüedad del cliente
Costo mensual
🖥️ Aplicación

Se desarrolló una aplicación interactiva con Streamlit que permite:

Ingresar datos de un cliente
Obtener predicción en tiempo real
Visualizar probabilidad de churn
⚠️ Limitaciones
El modelo utiliza un subconjunto simplificado de variables
No se realizó optimización avanzada de hiperparámetros
En un entorno productivo se integraría con datos reales en tiempo real
🛠️ Tecnologías
Python
Pandas
Scikit-learn
Streamlit
Joblib