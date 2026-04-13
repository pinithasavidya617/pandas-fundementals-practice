import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)
normal_data = np.random.normal(50, 10, 200)
outliers = np.array([150, -30, 180, 200, -50])
data = pd.DataFrame({"value": np.concatenate([normal_data, outliers])})

print(data.head())
# sns.boxplot(y="value", data=data)
# plt.show()
sns.histplot(data["value"], kde=True, bins=20)
plt.show()


print("=== IQR METHOD ===")
Q1 = data["value"].quantile(0.25)
Q3 = data["value"].quantile(0.75)
IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = data[(data["value"] < lower_bound) | (data["value"] > upper_bound)]
print(outliers)

print("=== Z Score Method ===")

mean = data["value"].mean()
std = data["value"].std()

data["z_score"] =  (data["value"] - mean) / std

outliers_z = data[abs(data["z_score"]) > 3]
print(outliers_z)
print(len(data))        # 205
print(len(outliers_z))  # 5

sns.boxplot(x=data["value"], color="skyblue")
plt.title("Boxplot of outliers")
plt.show()

#------------------------------------------
# Remove outliers


data_clean = data[
    (data["value"] >= lower_bound) & (data["value"] <= upper_bound)
]
print(data_clean)
sns.histplot(data_clean["value"], kde=True, bins=20)
plt.show()

# Cap outliers at the bounds (winsorization)
data["value_capped"] = data["value"].clip(lower=lower_bound, upper=upper_bound)
print(data.head())

# ------------------------
#Log-transform data

shift = abs(data["value"].min()) + 1
data["value_shifted"] = data["value"] + shift
# we prepare a shift value to make everything positive.
data["log_value"] = np.log(data["value_shifted"])
print(data.head())


import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(16, 10))

# 1️ Original
plt.subplot(2, 2, 1)
sns.histplot(data["value"], kde=True)
plt.title("Original Data")

# 2️ After removing outliers
plt.subplot(2, 2, 2)
sns.histplot(data_clean["value"], kde=True)
plt.title("After Removing Outliers")

# 3️ After capping (winsorization)
plt.subplot(2, 2, 3)
sns.histplot(data["value_capped"], kde=True)
plt.title("After Capping")

# 4️ After log transform
plt.subplot(2, 2, 4)
sns.histplot(data["log_value"], kde=True)
plt.title("After Log Transform")

plt.tight_layout()
plt.show()




plt.figure(figsize=(12, 6))

plt.subplot(1, 4, 1)
sns.boxplot(y=data["value"])
plt.title("Original")

plt.subplot(1, 4, 2)
sns.boxplot(y=data_clean["value"])
plt.title("Removed")

plt.subplot(1, 4, 3)
sns.boxplot(y=data["value_capped"])
plt.title("Capped")

plt.subplot(1, 4, 4)
sns.boxplot(y=data["log_value"])
plt.title("Log Transformed")

plt.tight_layout()
plt.show()