# 1. Import required libraries
import pandas as pd # type: ignore
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns # type: ignore


# 2. Load the dataset
df = pd.read_csv("customer_purchasing_behaviors.csv")


# 3. Display number of rows and columns
print("Shape of dataset:", df.shape)


# 4. Print column names
print("Column names:")
print(df.columns)


# 5. Display first 5 rows
print("First 5 rows:")
print(df.head())


# 6. Check data types
print("Data types:")
print(df.dtypes)


# 7. Check missing values
print("Missing values:")
print(df.isnull().sum())


# 8. Fill missing values in numerical columns using mean
num_cols = df.select_dtypes(include=np.number).columns
for col in num_cols:
    df[col].fillna(df[col].mean(), inplace=True)


# 9. Fill missing values in categorical columns using mode
cat_cols = df.select_dtypes(include='object').columns
for col in cat_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)


# 10. Verify no missing values remain
print("Missing values after filling:")
print(df.isnull().sum())


# 11. Mean of numerical columns
print("Mean values:")
print(df[num_cols].mean())


# 12. Median of numerical columns
print("Median values:")
print(df[num_cols].median())


# 13. Standard deviation
print("Standard deviation:")
print(df[num_cols].std())


# 14. Minimum and Maximum values
print("Minimum values:")
print(df[num_cols].min())

print("Maximum values:")
print(df[num_cols].max())


# 15. Summary statistics
print("Full summary:")
print(df.describe())


# 16. Histogram for purchase_amount
plt.figure()
plt.hist(df["purchase_amount"], bins=10)
plt.title("Histogram of purchase_amount")
plt.xlabel("purchase_amount")
plt.ylabel("Frequency")
plt.show()


# 17. Bar chart for loyality score distribution
df["loyalty_score"].value_counts().sort_index().plot(kind="bar")
plt.title("Customers by Loyalty Score")
plt.xlabel("Loyalty Score")
plt.ylabel("Count")
plt.show()


# 18. Box plot for purchase_amount
plt.figure()
plt.boxplot(df["purchase_amount"])
plt.title("Box Plot of purchase_amount")
plt.show()


# 19. Scatter plot between age and purchase_amount
plt.figure()
plt.scatter(df["age"], df["purchase_amount"])
plt.title("age vs purchase_amount")
plt.xlabel("age")
plt.ylabel("purchase_amount")
plt.show()


# 20. Correlation heatmap
plt.figure()
sns.heatmap(df[num_cols].corr(), annot=True)
plt.title("Correlation Heatmap")
plt.show()