# 💳 Online Payment Fraud Detection using Clustering

This project applies **unsupervised machine learning** to detect fraudulent online payment transactions. Fraudulent activities often appear as anomalies in financial datasets, and clustering helps group similar transactions while isolating suspicious ones.  

---

## 📖 Description
Online payment systems are highly vulnerable to fraud, making detection a critical challenge. This project leverages **clustering algorithms (KMeans, DBSCAN)** to identify suspicious transaction patterns without relying solely on labeled data.  

The workflow includes:
- **Data Preprocessing**: Handling missing values, encoding categorical variables, and scaling numerical features.  
- **Feature Engineering**: Creating new features such as balance differences and transaction ratios to highlight fraud signals.  
- **Clustering Models**: Applying KMeans and DBSCAN to detect anomalies.  
- **Visualization**: Using histograms, boxplots, correlation heatmaps, PCA scatterplots, and fraud frequency charts to explore fraud trends.  
- **Evaluation**: Measuring cluster quality with silhouette scores and comparing clusters against actual fraud labels (`isFraud`).  

This project demonstrates an **end-to-end pipeline**: from data wrangling and feature extraction to clustering, visualization, and evaluation. It highlights practical skills in anomaly detection, data storytelling, and ML deployment — making it a strong portfolio piece.

---

## 📂 Dataset
The dataset (`transactions.xlsx`) contains:
- Transaction type (`TRANSFER`, `CASH_OUT`, `PAYMENT`, etc.)
- Transaction amount
- Origin and destination balances
- Fraud indicator (`isFraud`)

---

## 🚀 How to Run

### Jupyter Notebook
```bash
pip install -r requirements.txt
jupyter notebook
