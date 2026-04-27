import pandas as pd

def cargar_datos(ruta):
    df = pd.read_csv(ruta)

    if "customerID" in df.columns:
        df = df.drop("customerID", axis=1)

    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df = df.dropna()

    df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

    return df


def preparar_variables(df):
    columnas = [
        "tenure",
        "MonthlyCharges",
        "Contract",
        "InternetService",
        "PaymentMethod",
        "OnlineSecurity",
        "TechSupport",
        "PaperlessBilling"
    ]

    df = df[columnas + ["Churn"]]

    df = pd.get_dummies(df, drop_first=True)

    X = df.drop("Churn", axis=1)
    y = df["Churn"]

    return X, y