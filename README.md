# 🛍️ Retail Sales Forecasting & Analytics

A data-driven forecasting and analytics project to predict monthly retail sales using time series models. Built using Python and SQL to extract insights, build predictive models, and support retail planning decisions.

---

## 📌 Project Objective

To analyze historical transaction data, understand sales trends, and accurately forecast future sales to support retail inventory and marketing strategies.

---

## 🧰 Tech Stack

- **Languages**: Python, SQL
- **Libraries**: pandas, matplotlib, seaborn, statsmodels, Prophet, scikit-learn
- **Tools**: Jupyter Notebook, Streamlit (planned), Git

---

## 📊 Exploratory Data Analysis

- Parsed over 500,000+ transactions from an e-commerce retail dataset
- Identified key trends in sales volume, price, and customer behavior
- Handled missing values and outliers (e.g., negative quantities, null customer IDs)
- Aggregated monthly sales and visualized trends using time series plots

---

## 📈 Forecasting Models Compared

| Model     | MAE (£)      | RMSE (£)     |
|-----------|--------------|--------------|
| **Naive** | 243,368.33   | 282,882.70   |
| **ARIMA** | 261,237.26   | 277,666.97   |
| **Prophet** | 261,540.60 | 307,022.62   |

- Despite its simplicity, the naive model performed competitively
- ARIMA provided slightly better RMSE than the baseline
- Prophet showed increased error possibly due to limited seasonal patterns

---

## ✅ Key Takeaways

- Established a baseline forecast accuracy of **£282K RMSE**
- Demonstrated ability to preprocess, model, and evaluate time series data
- Built multiple forecasting models and compared performance with error metrics

---

## 📂 Folder Structure

retail_sales_forecasting/
│
├── data/
│   ├── raw/                
│   └── processed/          
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── app/
│   └── dashboard.py
│
├── README.md
└── requirements.txt

---

## 📎 Dataset

- [Online Retail Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/online+retail)

---

## 📬 Contact

**Developer**: [Vamshi Krishna Reddy]  
📧 Email: [vamshikrishna.reddy555@gmail.com]  
🔗 Portfolio: [https://www.linkedin.com/in/vamshikrishna11/]

---
