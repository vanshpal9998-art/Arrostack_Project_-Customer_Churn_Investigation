import pandas as pd
from pathlib import Path

# ---------------------------------------
# 1. FILE PATH
# ---------------------------------------

DATA_PATH = Path("data/processed/customer_segmented_churn.csv")
REPORT_PATH = Path("reports/customer_churn_insights.txt")

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Segmented dataset not found. Run segmentation.py first."
    )

df = pd.read_csv(DATA_PATH)

REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

# ---------------------------------------
# 2. OVERALL BUSINESS METRICS
# ---------------------------------------

total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
retained_customers = (df["Churn"] == "No").sum()

churn_rate = churned_customers / total_customers * 100

print("\n========== CUSTOMER CHURN INSIGHTS ==========")

print("\n1. OVERALL BUSINESS METRICS")
print("Total Customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Retained Customers:", retained_customers)
print("Overall Churn Rate:", round(churn_rate, 2), "%")

# ---------------------------------------
# 3. CONTRACT-WISE CHURN ANALYSIS
# ---------------------------------------

print("\n2. CONTRACT-WISE CHURN RATE")

contract_analysis = (
    df.groupby("Contract")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print(contract_analysis.round(2))

# ---------------------------------------
# 4. TENURE-WISE CHURN ANALYSIS
# ---------------------------------------

print("\n3. TENURE-WISE CHURN RATE")

df["Tenure_Group"] = pd.cut(
    df["tenure"],
    bins=[-1, 12, 24, 48, 72],
    labels=["0-12 Months", "13-24 Months",
            "25-48 Months", "49-72 Months"]
)

tenure_analysis = (
    df.groupby("Tenure_Group", observed=False)["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
)

print(tenure_analysis.round(2))

# ---------------------------------------
# 5. PAYMENT-METHOD ANALYSIS
# ---------------------------------------

print("\n4. PAYMENT METHOD CHURN RATE")

payment_analysis = (
    df.groupby("PaymentMethod")["Churn"]
    .apply(lambda x: (x == "Yes").mean() * 100)
    .sort_values(ascending=False)
)

print(payment_analysis.round(2))

# ---------------------------------------
# 6. CUSTOMER SEGMENT ANALYSIS
# ---------------------------------------

print("\n5. CUSTOMER SEGMENT CHURN RATE")

segment_analysis = (
    df.groupby("Cluster")
    .agg(
        Customers=("customerID", "count"),
        Average_Tenure=("tenure", "mean"),
        Average_Monthly_Charges=("MonthlyCharges", "mean"),
        Churn_Rate=("Churn", lambda x: (x == "Yes").mean() * 100)
    )
    .round(2)
)

print(segment_analysis)

# ---------------------------------------
# 7. IDENTIFY HIGH-RISK GROUPS
# ---------------------------------------

highest_contract = contract_analysis.idxmax()
highest_contract_rate = contract_analysis.max()

highest_payment = payment_analysis.idxmax()
highest_payment_rate = payment_analysis.max()

highest_tenure_group = tenure_analysis.idxmax()
highest_tenure_rate = tenure_analysis.max()

highest_risk_cluster = segment_analysis["Churn_Rate"].idxmax()
highest_cluster_rate = segment_analysis.loc[
    highest_risk_cluster, "Churn_Rate"
]

print("\n6. HIGH-RISK CUSTOMER GROUPS")

print(
    f"Highest churn contract: {highest_contract} "
    f"({highest_contract_rate:.2f}%)"
)

print(
    f"Highest churn payment method: {highest_payment} "
    f"({highest_payment_rate:.2f}%)"
)

print(
    f"Highest churn tenure group: {highest_tenure_group} "
    f"({highest_tenure_rate:.2f}%)"
)

print(
    f"Highest churn cluster: {highest_risk_cluster} "
    f"({highest_cluster_rate:.2f}%)"
)

# ---------------------------------------
# 8. BUSINESS RECOMMENDATIONS
# ---------------------------------------

recommendations = [
    "1. Review month-to-month contract customers and offer suitable "
    "longer-term plans where appropriate.",

    "2. Contact customers during their early subscription period "
    "with onboarding support.",

    "3. Investigate payment difficulties and make payment options "
    "easier for customers.",

    "4. Review high-risk customer segments and offer relevant "
    "retention support.",

    "5. Monitor churn rate regularly to measure whether retention "
    "campaigns are effective."
]

print("\n7. BUSINESS RECOMMENDATIONS")

for recommendation in recommendations:
    print(recommendation)

# ---------------------------------------
# 9. SAVE BUSINESS INSIGHTS REPORT
# ---------------------------------------

with open(REPORT_PATH, "w", encoding="utf-8") as file:

    file.write("CUSTOMER CHURN INVESTIGATION REPORT\n")
    file.write("=" * 45 + "\n\n")

    file.write(f"Total Customers: {total_customers}\n")
    file.write(f"Churned Customers: {churned_customers}\n")
    file.write(f"Retained Customers: {retained_customers}\n")
    file.write(f"Overall Churn Rate: {churn_rate:.2f}%\n\n")

    file.write("CONTRACT-WISE CHURN RATE\n")
    file.write(contract_analysis.round(2).to_string())
    file.write("\n\nTENURE-WISE CHURN RATE\n")
    file.write(tenure_analysis.round(2).to_string())
    file.write("\n\nPAYMENT-METHOD CHURN RATE\n")
    file.write(payment_analysis.round(2).to_string())
    file.write("\n\nCUSTOMER SEGMENT ANALYSIS\n")
    file.write(segment_analysis.to_string())
    file.write("\n\nBUSINESS RECOMMENDATIONS\n")

    for recommendation in recommendations:
        file.write(recommendation + "\n")

print("\nInsights report saved at:", REPORT_PATH)
print("\n========== INSIGHTS ANALYSIS COMPLETED ==========")