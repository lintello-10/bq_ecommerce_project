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

## 🛠️ Tech Stack & Tools
* **SQL / Google BigQuery:** Data extraction, querying, and aggregation of nested/repeated structures.
* **Python:** Data manipulation and Exploratory Data Analysis (EDA).
* **Pandas & NumPy:** Data preprocessing and feature engineering.
* **Git & GitHub:** Version control and repository management.
* **VS Code:** Development environment.

## 🚀 Project Structure
```text
bq_ecommerce_project/
│
├── data/                    # Dataset directory (raw & processed)
│   └── ecommerce_users_raw.csv
│
├── notebooks/               # Jupyter Notebooks for EDA and modeling
│   └── .ipynb
│
├── .gitignore               # Excluded sensitive files and virtual environments
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation