# Customer Churn Investigation

## 1. Project Overview

Customer Churn Investigation is a data analytics project focused on understanding why customers leave a subscription-based service.

The project uses Python, data analysis, visualization, and machine learning techniques to identify churn patterns, analyze customer behavior, and group customers into meaningful segments.

The goal is to generate evidence-based insights that can help a business improve customer retention.

## 2. Business Problem

Customer churn affects business revenue and long-term growth.

A business needs to understand:
- How many customers are leaving?
- Which customer groups have higher churn rates?
- Does contract type influence customer churn?
- How do tenure and monthly charges relate to churn?
- Which customer segments may need retention strategies?

## 3. Project Objectives

- Understand the customer churn dataset.
- Identify and handle data quality issues.
- Perform exploratory data analysis (EDA).
- Analyze churn patterns across customer groups.
- Perform customer segmentation using K-Means.
- Validate processed data and project outputs.
- Generate business insights and recommendations.

## 4. Stakeholder

**Primary stakeholder:** Customer Retention Manager.

The analysis is designed to support customer retention decisions by identifying customer groups with higher churn rates.

## 5. Dataset Information

**Dataset:** IBM Telco Customer Churn

The original dataset contains approximately:
- 7,043 customer records
- 21 columns
- Customer demographics and service information
- Contract and payment information
- Charges and tenure
- Churn status

The processed dataset may contain an additional `Cluster` column after customer segmentation.

## 6. Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- K-Means Clustering
- StandardScaler
- Pytest
- Git and GitHub

## 7. Project Structure

```text
Arrowstack Project 1/
│
├── data/
│   ├── raw/
│   │   └── customer_churn.csv
│   └── processed/
│       ├── cleaned_churn.csv
│       └── segmented_churn.csv
│
├── src/
│   ├── data_understanding.py
│   ├── data_cleaning.py
│   ├── eda.py
│   ├── segmentation.py
│   ├── validation.py
│   └── insights.py
│
├── notebooks/
├── reports/
│   ├── figures/
│   ├── evidence/
│   └── customer_churn_insights.txt
│
├── docs/
│   ├── requirements.md
│   ├── project_architecture.md
│   ├── data_dictionary.md
│   ├── business_questions.md
│   └── decision_log.md
│
├── tests/
│   └── test_data_cleaning.py
│
├── requirements.txt
└── README.md
```

## 8. Installation and Setup

### Step 1: Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd "Arrowstack Project 1"
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### Step 2: Create a virtual environment

```bash
python3 -m venv .venv
```

### Step 3: Activate the environment

```bash
source .venv/bin/activate
```

### Step 4: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Place the dataset

Place the dataset at:

```text
data/raw/customer_churn.csv
```

## 9. Project Execution

Run commands from the project root directory.

### Step 1: Understand the dataset

```bash
python src/data_understanding.py
```

### Step 2: Clean the dataset

```bash
python src/data_cleaning.py
```

### Step 3: Perform exploratory data analysis

```bash
python src/eda.py
```

### Step 4: Perform customer segmentation

```bash
python src/segmentation.py
```

### Step 5: Validate the processed data

```bash
python src/validation.py
```

### Step 6: Generate business insights

```bash
python src/insights.py
```

### Step 7: Run automated tests

```bash
python -m pytest tests/ -v
```

## 10. Analysis and Outputs

The project produces:

- Dataset quality and summary information.
- Cleaned customer dataset.
- Churn distribution visualization.
- Contract-wise churn analysis.
- Tenure and monthly charges analysis.
- Payment method churn analysis.
- Customer segmentation results.
- Cluster profile visualizations.
- Data validation results.
- Automated test results.
- Business insights and retention recommendations.

Generated figures are saved in:

```text
reports/figures/
```

The business insights report is saved in:

```text
reports/customer_churn_insights.txt
```

## 11. Customer Segmentation

K-Means clustering is used to group customers based on selected behavioral and billing features.

The current clustering features are:
- Tenure
- Monthly Charges

StandardScaler is used to scale the selected features before clustering.

The silhouette score is used to compare candidate cluster counts.

**Note:** Customer segmentation is an unsupervised analysis. It does not predict whether an individual customer will churn.

## 12. Data Quality and Testing

The project includes checks for:

- Missing values.
- Duplicate records.
- Unique customer IDs.
- Valid tenure values.
- Non-negative charges.
- Numeric TotalCharges values.
- Valid churn categories.
- Required dataset columns.

Automated tests are available in the `tests/` directory.

## 13. Business Recommendations

Recommendations will be based on the actual analysis results.

Potential retention actions include:
- Investigating customer groups with higher churn rates.
- Reviewing contract options for high-risk customer groups.
- Improving onboarding for new customers.
- Reviewing payment-related customer experiences.
- Designing targeted retention campaigns.

These are areas to investigate, not claims that a particular factor causes churn.

## 14. Limitations

- The analysis uses a historical dataset.
- Results may not represent current customer behavior.
- Customer segmentation depends on the selected features.
- Clustering does not establish causal relationships.
- Retention recommendations require business testing.

## 15. Future Improvements

- Build a supervised machine learning churn prediction model.
- Add explainable AI techniques.
- Develop an interactive Streamlit dashboard.
- Add customer lifetime value analysis.
- Compare multiple clustering algorithms.
- Evaluate retention strategies using new business data.

## 16. Project Status

This project is being developed as part of the Arrowstack internship.

The objective is to deliver a reproducible, validated, and well-documented customer churn analysis workflow.

---

**Author:** Vansh Kumar

**Project:** Arrowstack Internship – Project 1

**Domain:** Data Analytics and Machine Learning