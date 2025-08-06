from sklearn.datasets import fetch_california_housing
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns


#Load California housing dataset
housing = fetch_california_housing(as_frame=True)

#Convert to DataFrame
df=housing.frame


#step 1 :Explore the dataset
print(df.head())
print(df.info())

# step 2:basic stattistics
print(df.describe())

# Step 3: Distribution of house prices
plt.figure(figsize=(8,5))
plt.hist(df['MedHouseVal'], bins=50, edgecolor="black")
plt.xlabel("Median House Value (in $100,000s)")
plt.ylabel("Number of Districts")
plt.title("Distribution of House Prices")
plt.show()

# step4:Scattwer plot of house prices vs. median income
plt.figure(figsize=(8,5))
plt.scatter(df['MedInc'], df['MedHouseVal'], alpha=0.3)
plt.xlabel("Median Income")
plt.ylabel("Median House Value")
plt.title("House Value vs Median Income")
plt.show()

# step5:Correlation heatmap
plt.figyre(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()