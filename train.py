import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, roc_auc_score, precision_recall_curve
from src.preprocess import cargar_datos, preparar_variables

# CARGA

df = cargar_datos("data/clientes.csv")
X, y = preparar_variables(df)

# ESCALADO

escalador = StandardScaler()
X[["tenure", "MonthlyCharges"]] = escalador.fit_transform(
    X[["tenure", "MonthlyCharges"]]
)

# SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# MODELO

modelo = LogisticRegression(max_iter=2000, class_weight="balanced")
modelo.fit(X_train, y_train)

# THRESHOLD 

y_proba = modelo.predict_proba(X_test)[:, 1]

precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
f1 = 2 * (precision * recall) / (precision + recall)
threshold_optimo = thresholds[f1.argmax()]

# GUARDADO

joblib.dump(modelo, "models/modelo.pkl")
joblib.dump(X.columns, "models/columnas.pkl")
joblib.dump(escalador, "models/escalador.pkl")
joblib.dump(threshold_optimo, "models/threshold.pkl")

joblib.dump(X_test, "models/X_test.pkl")
joblib.dump(y_test, "models/y_test.pkl")

print("✅ Modelo entrenado")

# MÉTRICAS

y_pred = (y_proba >= threshold_optimo).astype(int)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC:", roc_auc_score(y_test, y_proba))
print("Threshold óptimo:", threshold_optimo)