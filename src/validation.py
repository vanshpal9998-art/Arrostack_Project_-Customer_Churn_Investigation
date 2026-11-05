import pandas as pd
from pathlib import Path

# ---------------------------------------
# 1. FILE PATH
# ---------------------------------------

DATA_PATH = Path("data/processed/customer_segmented_churn.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Segmented dataset not found. Run segmentation.py first."
    )

df = pd.read_csv(DATA_PATH)

print("\n========== DATA VALIDATION STARTED ==========")


# ---------------------------------------
# 2. REQUIRED COLUMN CHECK
# ---------------------------------------

required_columns = [
    "customerID",
    "tenure",
    "MonthlyCharges",
    "TotalCharges",
    "Churn",
    "Cluster"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

assert not missing_columns, (
    f"Missing required columns: {missing_columns}"
)

print("\nPASS: All required columns are present.")


# ---------------------------------------
# 3. DATASET SHAPE CHECK
# ---------------------------------------

assert len(df) > 0, "Dataset is empty!"

print("PASS: Dataset is not empty.")
print("Dataset Shape:", df.shape)


# ---------------------------------------
# 4. DUPLICATE CHECK
# ---------------------------------------

duplicate_count = df.duplicated().sum()

print("\nDuplicate Records:", duplicate_count)

assert duplicate_count == 0, "Duplicate records found!"

print("PASS: No duplicate records.")


# ---------------------------------------
# 5. MISSING VALUE CHECK
# ---------------------------------------

missing_values = df.isnull().sum()

print("\nMissing Values:")
print(missing_values)

assert missing_values.sum() == 0, (
    "Missing values found in the dataset!"
)

print("PASS: No missing values.")


# ---------------------------------------
# 6. CUSTOMER ID CHECK
# ---------------------------------------

assert df["customerID"].is_unique, (
    "Duplicate customer IDs found!"
)

print("PASS: Customer IDs are unique.")


# ---------------------------------------
# 7. NUMERIC RANGE CHECKS
# ---------------------------------------

assert df["tenure"].between(0, 72).all(), (
    "Invalid tenure values found!"
)

assert (df["MonthlyCharges"] >= 0).all(), (
    "Negative monthly charges found!"
)

assert (df["TotalCharges"] >= 0).all(), (
    "Negative total charges found!"
)

print("PASS: Numeric values are within expected ranges.")


# ---------------------------------------
# 8. CHURN VALUE CHECK
# ---------------------------------------

valid_churn_values = {"Yes", "No"}

actual_churn_values = set(df["Churn"].dropna().unique())

assert actual_churn_values.issubset(valid_churn_values), (
    "Unexpected churn values found!"
)

print("PASS: Churn values are valid.")


# ---------------------------------------
# 9. CLUSTER CHECK
# ---------------------------------------

assert df["Cluster"].notnull().all(), (
    "Missing cluster labels found!"
)

assert pd.api.types.is_integer_dtype(df["Cluster"]), (
    "Cluster labels must be integers."
)

print("PASS: Cluster labels are valid.")


# ---------------------------------------
# 10. FINAL VALIDATION REPORT
# ---------------------------------------

print("\n========== VALIDATION SUMMARY ==========")
print("Total Customers:", len(df))
print("Total Columns:", len(df.columns))
print("Total Clusters:", df["Cluster"].nunique())
print("Total Churned Customers:", (df["Churn"] == "Yes").sum())
print("Total Retained Customers:", (df["Churn"] == "No").sum())

print("\nALL VALIDATION CHECKS PASSED!")
print("========== VALIDATION COMPLETED ==========")