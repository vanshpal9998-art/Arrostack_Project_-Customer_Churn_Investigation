import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


# ---------------------------------------
# 1. FILE PATHS
# ---------------------------------------

DATA_PATH = Path("data/processed/customer_churn_cleaned.csv")
OUTPUT_PATH = Path("data/processed/customer_segmented_churn.csv")
FIGURE_DIR = Path("reports/figures")

FIGURE_DIR.mkdir(parents=True, exist_ok=True)


# ---------------------------------------
# 2. LOAD DATASET
# ---------------------------------------

if not DATA_PATH.exists():
    raise FileNotFoundError(
        "Cleaned dataset not found. Run data_cleaning.py first."
    )

df = pd.read_csv(DATA_PATH)

print("\n========== CUSTOMER SEGMENTATION ==========")
print("\nDataset Shape:", df.shape)


# ---------------------------------------
# 3. SELECT FEATURES
# ---------------------------------------


features = ["tenure", "MonthlyCharges"]

X = df[features].copy()

if X.isnull().any().any():
    raise ValueError("Selected features contain missing values.")

if not (X.dtypes.apply(pd.api.types.is_numeric_dtype)).all():
    raise TypeError("Selected features must be numeric.")


# ---------------------------------------
# 4. FEATURE SCALING
# ---------------------------------------

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

print("\nFeature scaling completed!")


# ---------------------------------------
# 5. FIND BEST NUMBER OF CLUSTERS
# ---------------------------------------

silhouette_scores = []

cluster_range = range(2, 7)

for k in cluster_range:

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(X_scaled)

    score = silhouette_score(X_scaled, labels)

    silhouette_scores.append(score)

    print(f"Clusters: {k}, Silhouette Score: {score:.4f}")


best_k = list(cluster_range)[silhouette_scores.index(max(silhouette_scores))]

print("\nBest Number of Clusters:", best_k)


# ---------------------------------------
# 6. TRAIN FINAL K-MEANS MODEL
# ---------------------------------------

kmeans = KMeans(
    n_clusters=best_k,
    random_state=42,
    n_init=10
)

df["Cluster"] = kmeans.fit_predict(X_scaled)

print("\nCustomer clusters assigned successfully!")


# ---------------------------------------
# 7. CUSTOMER SEGMENT PROFILES
# ---------------------------------------

profile = df.groupby("Cluster").agg(
    Customer_Count=("customerID", "count"),
    Average_Tenure=("tenure", "mean"),
    Average_Monthly_Charges=("MonthlyCharges", "mean"),
    Average_Total_Charges=("TotalCharges", "mean"),
    Churn_Rate=("Churn", lambda x: (x == "Yes").mean() * 100)
).round(2)

print("\n========== CUSTOMER SEGMENT PROFILES ==========")
print(profile)


# ---------------------------------------
# 8. SAVE SEGMENTED DATASET
# ---------------------------------------

df.to_csv(OUTPUT_PATH, index=False)

print("\nSegmented dataset saved at:", OUTPUT_PATH)


# ---------------------------------------
# 9. SILHOUETTE SCORE CHART
# ---------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    list(cluster_range),
    silhouette_scores,
    marker="o"
)

plt.title("Silhouette Score for Customer Segmentation")
plt.xlabel("Number of Clusters")
plt.ylabel("Silhouette Score")
plt.xticks(list(cluster_range))
plt.savefig(FIGURE_DIR / "silhouette_scores.png", bbox_inches="tight")
plt.show()
plt.close()


# ---------------------------------------
# 10. CUSTOMER SEGMENT VISUALIZATION
# ---------------------------------------

plt.figure(figsize=(9, 6))

sns.scatterplot(
    data=df,
    x="tenure",
    y="MonthlyCharges",
    hue="Cluster",
    palette="Set2",
    s=60
)

plt.title("Customer Segmentation Using K-Means")
plt.xlabel("Tenure (Months)")
plt.ylabel("Monthly Charges")
plt.savefig(FIGURE_DIR / "customer_segments.png", bbox_inches="tight")
plt.show()
plt.close()


# ---------------------------------------
# 11. CHURN RATE BY CLUSTER
# ---------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(
    data=profile.reset_index(),
    x="Cluster",
    y="Churn_Rate"
)

plt.title("Customer Churn Rate by Segment")
plt.xlabel("Customer Segment")
plt.ylabel("Churn Rate (%)")
plt.savefig(FIGURE_DIR / "churn_by_segment.png", bbox_inches="tight")
plt.show()
plt.close()


print("\nAll segmentation charts saved successfully!")
print("\n========== SEGMENTATION COMPLETED ==========")
