<<<<<<< HEAD
<div align="center">

# 🛒 GA4 E-Commerce User Behavior & Purchase Prediction

**An end-to-end data science pipeline analyzing Google Analytics 4 data to predict user purchase intent.**  
*Built with BigQuery, Scikit-Learn, XGBoost, and Streamlit.*

[![BigQuery](https://img.shields.io/badge/Google%20Cloud-BigQuery-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com/bigquery)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://bqecommerceproject-up6hblseqvj8tggchxdfjt.streamlit.app/)
[![Status](https://img.shields.io/badge/Status-Live%20on%20Streamlit-46E3B7?style=for-the-badge&logo=streamlit&logoColor=white)](https://bqecommerceproject-up6hblseqvj8tggchxdfjt.streamlit.app/)

</div>

---

## 🚀 Live Demo & Web Application
> A machine learning web application built with Streamlit that predicts user conversion likelihood in real-time based on session behavior and demographics, incorporating insights from exploratory analysis (including top-performing countries).

* **🔗 [Access the Live Streamlit App](https://bqecommerceproject-up6hblseqvj8tggchxdfjt.streamlit.app/)**

---

## 📌 Project Overview
This project focuses on extracting, processing, and analyzing user behavior data from a large-scale Google Analytics 4 (GA4) e-commerce dataset hosted on Google Cloud BigQuery. The ultimate goal is to build a robust Machine Learning pipeline to predict whether a user will complete a purchase based on their browsing and interaction patterns.

### ✨ Dataset & Feature Engineering
The raw data is queried directly from Google Analytics 4 public tables (`bigquery-public-data.ga4_obfuscated_sample_ecommerce`). 
Using advanced SQL aggregation, the dataset is transformed from raw event-level rows into a clean, user-centric dataframe (`79,421 rows x 8 columns`), where each row represents a unique user profile (`user_pseudo_id`).

* **Contextual Features:** Device category (`device.category`), geographical location (`geo.country`), and traffic medium (`traffic_source.medium`).
* **Behavioral Features:** Action counters representing key funnel milestones (`view_item`, `add_to_cart`, `begin_checkout`).
* **Target Variable (`target_has_purchased`):** Binary classification target indicating whether a user completed at least one purchase (`1`) or not (`0`).

---

## 🛠️ Tech Stack & Tools
* **SQL / Google BigQuery:** Data extraction, querying, and aggregation of nested/repeated structures.
* **Python:** Data manipulation and Exploratory Data Analysis (EDA).
* **Pandas & NumPy:** Data preprocessing and feature engineering.
* **Scikit-Learn:** Machine Learning model training and inference.
* **Streamlit:** Web application framework and UI deployment.
* **Git & GitHub:** Version control and repository management.
* **VS Code:** Development environment.

---

## 📁 Project Structure
```text
bq_ecommerce_project/
│
├── data/                  # Dataset directory (raw & processed)
│   └── ecommerce_users_raw.csv
│
├── notebooks/             # Jupyter Notebooks for EDA and modeling
│   └── .ipynb
│
├── app.py                 # Main Streamlit web application
├── model.pkl              # Trained machine learning model
├── .gitignore             # Excluded sensitive files and virtual environments
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
=======
# 🛒 GA4 E-Commerce User Behavior & Purchase Prediction

## 📌 Project Overview
This project focuses on extracting, processing, and analyzing user behavior data from a large-scale Google Analytics 4 (GA4) e-commerce dataset hosted on Google Cloud BigQuery. The ultimate goal is to build a robust Machine Learning pipeline to predict whether a user will complete a purchase based on their browsing and interaction patterns.

## 📂 Dataset & Feature Engineering
The raw data is queried directly from Google Analytics 4 public tables (`bigquery-public-data.ga4_obfuscated_sample_ecommerce`). 
Using advanced SQL aggregation, the dataset is transformed from raw event-level rows into a clean, user-centric dataframe (`79,421 rows x 8 columns`), where each row represents a unique user profile (`user_pseudo_id`).

### Key Features Extracted:
* **Contextual Features:** Device category (`device.category`), geographical location (`geo.country`), and traffic medium (`traffic_source.medium`).
* **Behavioral Features:** Action counters representing key funnel milestones (`view_item`, `add_to_cart`, `begin_checkout`).
* **Target Variable (`target_has_purchased`):** Binary classification target indicating whether a user completed at least one purchase (`1`) or not (`0`).

---

## 🚀 Live Demo & Web Application
> A machine learning web application built with Streamlit that predicts user conversion likelihood in real-time based on session behavior and demographics, incorporating insights from exploratory analysis (including top-performing countries).

* Try out the live application here: **[E-commerce Conversion Predictor App](https://bqecommerceproject-up6hblseqvj8tggchxdfjt.streamlit.app/)**

---

## 🛠️ Tech Stack & Tools
* **SQL / Google BigQuery:** Data extraction, querying, and aggregation of nested/repeated structures.
* **Python:** Data manipulation and Exploratory Data Analysis (EDA).
* **Pandas & NumPy:** Data preprocessing and feature engineering.
* **Scikit-Learn:** Machine Learning model training and inference.
* **Streamlit:** Web application framework and UI deployment.
* **Git & GitHub:** Version control and repository management.
* **VS Code:** Development environment.

## 🚀 Project Structure
```text
bq_ecommerce_project/
│
├── data/                  # Dataset directory (raw & processed)
│   └── ecommerce_users_raw.csv
│
├── notebooks/             # Jupyter Notebooks for EDA and modeling
│   └── .ipynb
│
├── app.py                 # Main Streamlit web application
├── model.pkl              # Trained machine learning model
├── .gitignore             # Excluded sensitive files and virtual environments
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
>>>>>>> 5811545 (Revising the whole code)
