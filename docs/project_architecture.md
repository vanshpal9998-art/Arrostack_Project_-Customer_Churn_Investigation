# Customer Churn Investigation
## Project Architecture and Workflow

### 1. Architecture Overview

The project follows a modular data science workflow.

Raw customer data is loaded, inspected, cleaned, analyzed,
segmented, validated and converted into business insights.

### 2. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Data visualization |
| Seaborn | Statistical visualization |
| Scikit-learn | Customer segmentation |
| Jupyter | Interactive analysis |
| Git | Version control |

### 3. Project Architecture

```text
Customer Churn Investigation
             |
             v
      Raw Customer Data
             |
             v
    Data Understanding
             |
             v
       Data Cleaning
             |
             v
     Cleaned Dataset
             |
       +-----+------+
       |            |
       v            v
      EDA       K-Means
       |       Segmentation
       |            |
       +-----+------+
             |
             v
       Data Validation
             |
             v
      Business Insights
             |
             v
  Retention Recommendations
             |
             v
      Final Project Report
```

### 4. Folder Structure

```text
Arrowstack Project 1/
│
├── data/
│   ├── raw/
│   │   └── customer_churn.csv
│   │
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
│
├── reports/
│   ├── figures/
│   └── customer_churn_insights.txt
│
├── docs/
│   ├── data_dictionary.md
│   ├── business_questions.md
│   ├── decision_log.md
│   ├── requirements.md
│   └── project_architecture.md
│
├── tests/
│
├── requirements.txt
└── README.md
```

### 5. Module Responsibilities

#### Module 1: Data Understanding

File: src/data_understanding.py

- Loads the raw dataset.
- Checks dataset dimensions.
- Inspects columns and data types.
- Identifies missing values and duplicates.
- Examines churn distribution.

#### Module 2: Data Cleaning

File: src/data_cleaning.py

- Removes duplicate records.
- Converts TotalCharges to numeric format.
- Handles missing TotalCharges values.
- Saves the cleaned dataset.

#### Module 3: Exploratory Data Analysis

File: src/eda.py

- Analyzes churn distribution.
- Compares churn by contract type.
- Examines customer tenure.
- Investigates monthly charges and payment methods.
- Generates charts.

#### Module 4: Customer Segmentation

File: src/segmentation.py

- Selects customer features.
- Applies StandardScaler.
- Evaluates cluster counts using silhouette scores.
- Applies K-Means.
- Saves customer segment labels.

#### Module 5: Data Validation

File: src/validation.py

- Checks required columns.
- Checks missing values and duplicates.
- Validates customer IDs.
- Checks numeric ranges and cluster labels.

#### Module 6: Business Insights

File: src/insights.py

- Calculates churn metrics.
- Compares churn across customer groups.
- Identifies high-risk segments.
- Generates retention recommendations.

### 6. Data Flow

**Input:** Raw customer CSV file.

**Processing:** Data understanding, cleaning, EDA,
segmentation and validation.

**Output:**
- Cleaned CSV file.
- Segmented CSV file.
- EDA charts.
- Business insights report.
- Retention recommendations.

### 7. Reproducibility

To reproduce the analysis:

1. Install the dependencies from requirements.txt.
2. Place the raw CSV in data/raw/.
3. Run the scripts in the documented order.
4. Review generated datasets and charts.
5. Run validation and automated tests.
6. Review the final business insights.

### 8. Security and Data Integrity

- Keep raw data unchanged.
- Do not publish private customer information.
- Avoid committing virtual environments to Git.
- Validate input files before analysis.
- Keep generated outputs separate from raw data.

### 9. Future Architecture Improvements

- Add automated pipeline execution.
- Introduce supervised churn prediction.
- Build an interactive Streamlit dashboard.
- Add logging and automated monitoring.
- Support larger datasets and scheduled analysis.
-