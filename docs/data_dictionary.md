# Customer Churn Investigation
## Data Dictionary

### 1. Project Overview

This dataset contains customer information for a telecommunications
company. It includes customer demographics, subscription services,
billing information, and churn status.

The purpose of this investigation is to identify customer churn
patterns, understand customer segments, and recommend retention
strategies.

### 2. Dataset Information

- Dataset: IBM Telco Customer Churn
- File: customer_churn.csv
- Original records: 7,043
- Original columns: 21
- Target variable: Churn

### 3. Column Descriptions

| Column Name | Description | Data Type |
|---|---|---|
| customerID | Unique customer identifier | String |
| gender | Customer gender | Categorical |
| SeniorCitizen | Whether customer is a senior citizen (0 or 1) | Integer |
| Partner | Whether customer has a partner | Categorical |
| Dependents | Whether customer has dependents | Categorical |
| tenure | Number of months the customer has stayed | Integer |
| PhoneService | Whether phone service is active | Categorical |
| MultipleLines | Whether customer has multiple phone lines | Categorical |
| InternetService | Type of internet service | Categorical |
| OnlineSecurity | Whether online security is active | Categorical |
| OnlineBackup | Whether online backup is active | Categorical |
| DeviceProtection | Whether device protection is active | Categorical |
| TechSupport | Whether technical support is active | Categorical |
| StreamingTV | Whether streaming TV is active | Categorical |
| StreamingMovies | Whether streaming movies is active | Categorical |
| Contract | Customer contract type | Categorical |
| PaperlessBilling | Whether paperless billing is enabled | Categorical |
| PaymentMethod | Customer payment method | Categorical |
| MonthlyCharges | Monthly subscription charges | Float |
| TotalCharges | Total charges accumulated | Float |
| Churn | Whether customer left the company | Categorical |

### 4. Target Variable

**Churn** is the target variable.

- Yes: Customer discontinued the service.
- No: Customer continued the service.

### 5. Additional Project Columns

The following column is added during customer segmentation:

| Column Name | Description |
|---|---|
| Cluster | Customer segment assigned by K-Means |

### 6. Important Data Quality Considerations

1. TotalCharges may contain blank values.
2. TotalCharges must be converted into numeric format.
3. Duplicate customer records must be checked.
4. Customer IDs should be unique.
5. Tenure should contain valid non-negative values.
6. MonthlyCharges and TotalCharges should not be negative.
7. Churn should contain only Yes or No.

### 7. Analytical Features

The project uses the following features for customer segmentation:

- tenure
- MonthlyCharges

The Churn column is excluded from clustering to prevent target leakage.

### 8. Limitations

- The dataset represents a particular telecommunications business.
- Historical customer behaviour may not predict future behaviour perfectly.
- Customer churn patterns do not prove causal relationships.
- Retention recommendations should be tested before implementation.

### 9. Business Objective

Identify customer groups with higher churn rates and recommend
data-driven retention strategies to improve customer retention.