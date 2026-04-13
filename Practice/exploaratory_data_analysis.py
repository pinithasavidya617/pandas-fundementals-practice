import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

df = sns.load_dataset("tips")
print(df.head(10))
print(df["tip"].mean())

df["tip_pct"] = (df["tip"] / df["total_bill"]) * 100
print(df.groupby("sex")["tip_pct"].mean())

print(df["total_bill"].corr(df["tip"]))

# sns.scatterplot(x="total_bill", y="tip", data=df)
# plt.show()
#
# sns.regplot(x="total_bill", y="tip", data=df)
# plt.show()

print(df["size"].value_counts(normalize=True) * 100)
# sns.countplot(x="size", data=df)
# plt.show()

print(df.groupby("size")["tip"].mean())
# Tip increases with party size

sns.histplot(df["total_bill"], kde=True, bins=20)
plt.title("Histogram of total bills")
plt.show()

sns.boxplot(x="day", y="tip", data=df)
plt.title("Tip Distribution by Day")
plt.show()
# Box = middle 50% (Q1–Q3)
#  Line inside = median
# Points outside = outliers
# Whiskers = range (excluding outliers)

sns.scatterplot(x="total_bill", y="tip", hue="smoker", data=df)
plt.title("Total Bill vs Tip (Smoker vs Non-Smoker)")
plt.show()

sns.lmplot(x="total_bill", y="tip", hue="smoker", data=df)
plt.show()

numeric_df = df.select_dtypes(include=["number"])
corr = numeric_df.corr()
sns.heatmap(corr, annot=True, cmap="YlOrRd", fmt=".2f")
plt.title("Correlation Heatmap")
# Each cell = correlation between two variables
plt.show()