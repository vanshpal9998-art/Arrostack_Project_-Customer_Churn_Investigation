import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Define paths
DATA_PATH = Path("data/processed/customer_churn_cleaned.csv")
OUTPUT_DIR = Path("reports/figures")

# check dataset
if not DATA_PATH.exists():
    raise FileNotFoundError(" Cleaned Dataset not found.")

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Load Cleaned dataset
df = pd.read_csv(DATA_PATH)

# set visualize style
sns.set_theme(style="whitegrid")

# Basic information

print("\n Dataset Shape:", df.shape)

print("\n Churn Distribution:")
print(df['Churn'].value_counts())

# calculate churn rate
churn_rate = (df['Churn'] == "yes").mean()*100
print("\nOverall churn Rate:", round(churn_rate, 2),"%")

# churn Distribution Plot
plt.figure(figsize=(7,5))
sns.countplot(data=df, x="Churn")

plt.title("Customer Churn Distribution")
plt.xlabel("Churn Status")
plt.ylabel("Number of Customers")
plt.savefig(OUTPUT_DIR / "churn_distribution.png")
plt.show()
plt.close()

# Contract VS Churn

contract_churn = pd.crosstab(
    df["Contract"],
    df["Churn"],
    normalize = "index"
)*100

print("\n Contract-wise churn percentage:")
print(contract_churn)

contract_churn.plot(
    kind="bar",
    stacked=True,
    figsize=(9,5)
)

plt.title("Contract Type vs Customer Churn")
plt.xlabel("Contract Type")
plt.ylabel("Percentage of Customers")
plt.xticks(rotation=0)
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "contract_vs_churn.png")
plt.show()
plt.close()

# Tenure VS Churn 

plt.figure(figsize=(9,5))
sns.boxplot(
    data= df,
    x= "Churn",
    y="tenure")
plt.title("Tenure Distribution by Churn Status")
plt.xlabel("churn Status")
plt.ylabel("Tenure (Months)")
plt.savefig(OUTPUT_DIR / "tenure_vs_churn.png")
plt.show()
plt.close()

# monthly charge vs churn

plt.figure(figsize=(9,5))
sns.boxplot(
    data=df,
    x="Churn",
    y="MonthlyCharges"
)
plt.title("Monthly Charges VS churn")
plt.xlabel("Churn Status")
plt.ylabel("Montly Charges")
plt.savefig(OUTPUT_DIR / "monthly_charges_vs_churn.png")
plt.show()
plt.close()

# payment method VS churn

payment_churn = pd.crosstab(
    df["PaymentMethod"],
    df["Churn"],
    normalize = "index"
)*100

print("\n Payment Method-wise churn percentage:")
print(payment_churn)

payment_churn.plot(
    kind="bar",
    stacked=True,
    figsize=(11,6)
)

plt.title("Payment Method vs Customer Churn")
plt.xlabel("Payment Method")
plt.ylabel("Percentage of Customers")
plt.xticks(rotation=30, ha="right")
plt.legend(title="Churn")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "payment_method_vs_churn.png")
plt.show()
plt.close()


# Correlation Heatmap

numeric_df = df.select_dtypes(include="number")

plt.figure(figsize=(10,8))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f")

plt.title("Numerical FeatureCorrelation Heatmap")
plt.tight_layout()
plt.savefig(OUTPUT_DIR / "correlation_heatmap.png")
plt.show()
plt.close()

# final output
print("\nEDA GRAPH FILES SAVED:")
for file in OUTPUT_DIR.glob("*.png"):
    print(file)