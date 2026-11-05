# Customer Churn Investigation
## Project Requirements Document

### 1. Project Information

- Project Name: Customer Churn Investigation
- Organization: Arrowstack
- Project Type: Foundation / Core Industry Task
- Programming Language: Python
- Domain: Data Science and Customer Analytics
- Dataset: IBM Telco Customer Churn

### 2. Problem Statement

The telecommunications company wants to understand why
customers discontinue their subscriptions.

This project analyzes historical customer information to
identify churn patterns, segment customers, and recommend
retention strategies.

### 3. Primary Stakeholder

Customer Retention Manager.

The stakeholder will use the analysis to identify customer
groups that may need additional retention support.

### 4. Project Inputs

- Customer demographics
- Subscription information
- Service details
- Contract information
- Payment methods
- Monthly charges
- Total charges
- Customer churn status

Input file:
data/raw/customer_churn.csv

### 5. Project Outputs

1. Cleaned customer dataset.
2. Exploratory data analysis charts.
3. Customer segmentation results.
4. Data validation results.
5. Customer churn insights report.
6. Business recommendations.
7. Project documentation.

### 6. Functional Requirements

FR-01: The system must load the customer dataset.

FR-02: The system must inspect dataset structure and data types.

FR-03: The system must identify missing values and duplicates.

FR-04: The system must clean invalid data appropriately.

FR-05: The system must save the cleaned dataset.

FR-06: The system must calculate the overall churn rate.

FR-07: The system must analyze churn using business questions.

FR-08: The system must generate EDA visualizations.

FR-09: The system must group customers using K-Means.

FR-10: The system must validate the processed dataset.

FR-11: The system must generate business insights.

FR-12: The system must recommend customer retention actions.

### 7. Non-Functional Requirements

- Code should be readable and organized.
- Scripts should be repeatable.
- File paths should be clearly defined.
- Errors should provide useful messages.
- Data should not be modified without justification.
- Documentation should explain how to run the project.
- Results should be reproducible using a fixed random seed.

### 8. Quality Requirements

- Customer IDs should be unique.
- Duplicate records should be checked.
- Missing values should be investigated.
- Numeric values should follow expected ranges.
- Churn values should be valid.
- Segmentation results should be evaluated.
- Important analytical findings should have supporting evidence.

### 9. Success Metrics

| Metric | Success Condition |
|---|---|
| Dataset loading | Dataset loads successfully |
| Data cleaning | Cleaning rules execute successfully |
| Duplicate check | No unexplained duplicates |
| Missing values | No unexplained missing values |
| EDA | Required business questions analyzed |
| Segmentation | Customers receive valid cluster labels |
| Validation | All documented checks pass |
| Documentation | Required project documents are available |
| Reproducibility | Another user can follow the run instructions |

### 10. Constraints

- Analysis uses the supplied historical dataset.
- Findings may not represent every telecommunications company.
- K-Means results depend on feature selection and scaling.
- Historical associations do not establish causation.
- The project does not provide real-time churn predictions.

### 11. Acceptance Criteria

The project is accepted when:

1. All required scripts execute successfully.
2. Cleaned and segmented datasets are generated.
3. EDA charts and insight reports are available.
4. Data quality checks pass.
5. Business questions are answered using actual results.
6. Limitations and recommendations are documented.
7. Automated tests are executed and recorded.
8. README instructions allow another user to reproduce the workflow.
9. Source code and evidence are organized.
10. The intern can explain the methodology and decisions.

### 12. Future Enhancements

- Predict customer churn using supervised machine learning.
- Compare multiple clustering algorithms.
- Build an interactive Streamlit dashboard.
- Automate data quality monitoring.
- Evaluate retention campaigns through experiments.
-