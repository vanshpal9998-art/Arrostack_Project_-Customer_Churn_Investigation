import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw/customer_churn.csv")
PROCESSED_PATH = Path("data/processed/customer_churn_cleaned.csv")

if not RAW_PATH.exists():
    raise FileNotFoundError("Raw dataset not found!")

df = pd.read_csv(RAW_PATH)

print("\n Original Dataset Shape:", df.shape)

print("\n Missing Values Before Cleaning:", df.isnull().sum().sum())

duplicates = df.duplicated().sum()
print("\n Duplicate Records:", duplicates)

df = df.drop_duplicates()

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

print("\n Missing Values After Type Conversion:", df.isnull().sum().sum())

## Handle missing TotalCharge 
# Blank TotalCharges for Zero tenure customers are replaced with 0 only after verifivation

zero_tenure = df["tenure"] == 0
df.loc[
    zero_tenure & df["TotalCharges"].isnull(),"TotalCharges"
] = 0

# Handle any missing vlaues
remmaining_missing = df.isnull().sum().sum()

if remmaining_missing > 0:
    median_value = df["TotalCharges"].median()
    df["TotalCharges"] = df["TotalCharges"].fillna(median_value)
    
# check invalid values
print("\n Invalid Values:")
print(df[~df["tenure"].between(0,1000)])

print("\nInvalid Monthly charges:")
print(df[df["MonthlyCharges"] < 0])

print("\nFinal Missing Values:")
print(df.isnull().sum())

# Save cleaned dataset
PROCESSED_PATH.parent.mkdir(parents=True, exist_ok = True)
df.to_csv(PROCESSED_PATH, index=False)

# Final dataset information 
print("\n Cleaned Dataset Saved Successfully!")
print("Location:", PROCESSED_PATH)