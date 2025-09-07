import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score, confusion_matrix
from scripts.utils import save_metrics

def run_model(df: pd.DataFrame):
    """Train and evaluate a Random Forest model on survival prediction."""

    # Encode categorical variables
    df_encoded = df.copy()
    for col in ["Gender", "Tumor_Type", "Biopsy_Result", "Treatment"]:
        df_encoded[col] = LabelEncoder().fit_transform(df_encoded[col])

    # Features and target
    X = df_encoded[["Age", "Gender", "Tumor_Size_cm", "Tumor_Type", "Treatment"]]
    y = LabelEncoder().fit_transform(df_encoded["Survival_Status"])

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:, 1]

    # Evaluation metrics
    metrics = {
        "Accuracy": accuracy_score(y_test, y_pred),
        "ROC-AUC": roc_auc_score(y_test, y_proba),
        "Confusion Matrix": confusion_matrix(y_test, y_pred).tolist()
    }

    # Save metrics via utils helper
    save_metrics(metrics)

    # Print metrics
    print("\nModel Performance:")
    for k, v in metrics.items():
        print(k, ":", v)
