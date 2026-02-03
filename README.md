# 💳 Transaction Fraud Detection App

An interactive **Streamlit application** that detects fraudulent transactions using **Logistic Regression**.  
This project demonstrates end‑to‑end machine learning: data preprocessing, feature engineering, model training, evaluation, and deployment in a user‑friendly dashboard.

---

## 📂 Project Structure
- `app1.py` → Streamlit app
- `transactions.xlsx` → Sample dataset
- `requirements.txt` → Dependencies
- `README.md` → Documentation

---

## 📊 Dataset
The dataset contains transaction records with the following columns:
- **step**: Time step of the transaction
- **type**: Transaction type (TRANSFER, CASH_OUT, PAYMENT, etc.)
- **amount**: Transaction amount
- **nameOrig**: Origin account
- **oldbalanceOrg / newbalanceOrig**: Origin account balances
- **nameDest**: Destination account
- **oldbalanceDest / newbalanceDest**: Destination account balances
- **isFraud**: Target variable (1 = Fraud, 0 = Legitimate)

---

## 🛠 Feature Engineering
New features created to improve fraud detection:
- `balance_diff_orig` = oldbalanceOrg − newbalanceOrig  
- `balance_diff_dest` = newbalanceDest − oldbalanceDest  
- `amount_ratio` = amount / (oldbalanceOrg + 1)

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Handle missing values
   - Encode categorical variables (`type`, `nameOrig`, `nameDest`)
2. **Feature Engineering**
   - Create balance differences and ratios
3. **Train/Test Split**
   - Stratified split to preserve fraud/non‑fraud ratio
4. **Scaling**
   - Standardize features with `StandardScaler`
5. **Model Training**
   - Logistic Regression baseline
6. **Evaluation**
   - Accuracy, Precision, Recall, F1‑score
   - Confusion Matrix visualization

---

## 🚀 Streamlit App Features
- Upload your own Excel dataset
- View raw and feature‑engineered data
- Train Logistic Regression model
- Display accuracy and classification report
- Interactive confusion matrix heatmap

---

## 📈 Sample Results
- **Accuracy**: ~92%
- **Precision (Fraud)**: 1.00
- **Recall (Fraud)**: 0.75  
Shows strong detection ability, with room to improve recall using advanced models.

---

## 🔮 Future Improvements
- Add model selection (Random Forest, XGBoost, etc.)
- Handle class imbalance (SMOTE, class weights)
- Plot ROC curve & AUC
- Feature importance visualization
- Real‑time transaction prediction form

---

## 🖥️ How to Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app1.py
