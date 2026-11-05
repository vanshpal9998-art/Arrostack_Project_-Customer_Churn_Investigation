import pandas as pd
import numpy as np
from pathlib import Path

DATA_PATH = Path("data/raw/customer_churn.csv")

if not DATA_PATH.exists():
    raise FileNotFoundError("Dataset not found!")

df = pd.read_csv(DATA_PATH)

print("Customer Churn Investigation")
print("Dataset loaded successfully!")

print("\n Dataset Shape:")
print(df.shape)

print("\n First Five Records:")
print(df.head())

print("\n Column Names:")
print(df.columns.tolist())

print("\n Data Types:")
print(df.dtypes)

print("\n Dataset Information:")
print(df.info())

print("\n Statistical Summary:")
print(df.describe(include='all'))

print("\n Missing Values:")
print(df.isnull().sum())

print("\n Duplicate Records:")
print(df.duplicated().sum())

print("\n Churn Distribution:")
print(df['Churn'].value_counts())

print("\n Churn Percentage:")
print(df['Churn'].value_counts(normalize=True) * 100)
