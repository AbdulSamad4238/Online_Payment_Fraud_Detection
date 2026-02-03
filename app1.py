
import streamlit as st
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------
# Streamlit Page Config
# ---------------------------
st.set_page_config(page_title="Fraud Detection App", layout="wide")

st.title("💳 Transaction Fraud Detection")
st.write("Upload transaction data and train a Logistic Regression model to detect fraud.")

# ---------------------------
# File Upload
# ---------------------------
uploaded_file = st.file_uploader("Upload transactions Excel file", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file)
    st.subheader("📊 Raw Dataset")
    st.dataframe(df.head())

    # ---------------------------
    # Data Preprocessing
    # ---------------------------
    df.fillna(0, inplace=True)

    encoder = LabelEncoder()
    df['type'] = encoder.fit_transform(df['type'])
    df['nameOrig'] = encoder.fit_transform(df['nameOrig'])
    df['nameDest'] = encoder.fit_transform(df['nameDest'])

    # Feature Engineering
    df['balance_diff_orig'] = df['oldbalanceOrg'] - df['newbalanceOrig']
    df['balance_diff_dest'] = df['newbalanceDest'] - df['oldbalanceDest']
    df['amount_ratio'] = df['amount'] / (df['oldbalanceOrg'] + 1)

    st.subheader("🛠 Feature Engineered Data")
    st.dataframe(df.head())

    # ---------------------------
    # Train-Test Split
    # ---------------------------
    y = df['isFraud']
    X = df.drop(['isFraud', 'nameOrig', 'nameDest'], axis=1)

    X['type'] = X['type'].astype('category').cat.codes

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # ---------------------------
    # Model Training
    # ---------------------------
    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    # ---------------------------
    # Evaluation
    # ---------------------------
    st.subheader("📈 Model Performance")

    acc = accuracy_score(y_test, y_pred)
    st.metric("Accuracy", f"{acc:.4f}")

    st.text("Classification Report")
    st.text(classification_report(y_test, y_pred))

    # Confusion Matrix
    cm = confusion_matrix(y_test, y_pred)

    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")

    st.pyplot(fig)

else:
    st.info("👆 Upload an Excel file to get started.")
