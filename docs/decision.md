# Customer Churn Investigation
## Project Decision Log

This document records important decisions made during the
Customer Churn Investigation project.

### Decision 1: Dataset Selection

**Decision:** Use the IBM Telco Customer Churn dataset.

**Reason:**
- Contains customer subscription information.
- Includes billing and service details.
- Provides a Churn column for analysis.
- Suitable for customer retention investigation.

### Decision 2: Programming Language

**Decision:** Use Python.

**Reason:**
- Supports data analysis and visualization.
- Provides libraries for machine learning.
- Makes the workflow repeatable.

### Decision 3: Data Analysis Libraries

**Decision:** Use Pandas, NumPy, Matplotlib and Seaborn.

**Reason:**
- Pandas: Data cleaning and manipulation.
- NumPy: Numerical operations.
- Matplotlib: Data visualization.
- Seaborn: Statistical visualization.

### Decision 4: Missing Value Handling

**Decision:** Convert TotalCharges into numeric format.

**Reason:**
Some TotalCharges values contain blank strings.

For customers with zero tenure and blank TotalCharges,
the value is interpreted as zero.

Other missing values must be investigated rather than
automatically replaced without justification.

### Decision 5: Feature Scaling

**Decision:** Use StandardScaler before K-Means clustering.

**Reason:**
Tenure and MonthlyCharges have different numerical scales.
Scaling prevents one feature from dominating because of its units.

### Decision 6: Customer Segmentation

**Decision:** Use K-Means clustering.

**Reason:**
- Groups customers based on similarities.
- Helps identify different customer profiles.
- Provides useful information for retention analysis.

### Decision 7: Clustering Features

**Decision:** Use tenure and MonthlyCharges.

**Reason:**
These features represent customer subscription duration
and monthly spending.

The Churn column is excluded from clustering because
the objective is to discover customer groups independently
of their churn outcome.

### Decision 8: Number of Clusters

**Decision:** Compare cluster counts from 2 to 6
using the silhouette score.

**Reason:**
The silhouette score helps evaluate how well-separated
the customer groups are.

The final number of clusters is selected from the
highest observed score.

### Decision 9: Data Validation

**Decision:** Create a separate validation module.

**Reason:**
It checks missing values, duplicates, customer IDs,
numeric ranges and cluster labels.

### Decision 10: Business Recommendations

**Decision:** Base recommendations on observed churn patterns.

**Reason:**
Business recommendations should be supported by
analysis rather than assumptions.

### Future Improvements

- Test alternative clustering algorithms.
- Include more customer features in segmentation.
- Evaluate retention strategies using experiments.
- Develop a predictive churn model.
- Build an interactive business dashboard.
-