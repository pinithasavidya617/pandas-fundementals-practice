import numpy as np
import pandas as pd

ecommerce = pd.DataFrame({
    "order_id": range(1, 101),
    "customer_id": np.random.randint(1, 30, 100),
    "order_date": pd.date_range("2024-01-01", periods=100, freq="D"),
    "product_category": np.random.choice(
        ["Electronics", "Clothing", "Books"], 100
    ),
    "quantity": np.random.randint(1, 10, 100),
    "unit_price": np.random.uniform(5, 200, 100).round(2),
    "customer_age": np.random.randint(18, 70, 100),
    "is_returned": np.random.choice([0, 1], 100, p=[0.85, 0.15])
})

df = ecommerce
print(df.head())

df["total_amount"] = df["quantity"] * df["unit_price"]
df["day_of_week"] = df["order_date"].dt.day_name()
df["is_weekend"] = df["order_date"].dt.dayofweek >= 5
df["month"] = df["order_date"].dt.month_name()

bins = [18, 30, 50, 100]
labels = ["Young", "Adult", "Senior"]
df["age_group"] = pd.cut(df["customer_age"], bins=bins, labels=labels)

df["high_value_order"] = df["total_amount"] > 500
# df["high_value_order"] = np.where(df["total_amount"] > 500, True, False)

df["total_orders"] = df.groupby("customer_id")["order_id"].transform("count")
df["avg_order_value"] = df.groupby("customer_id")["total_amount"].transform("mean")
return_rate = df.groupby("cust"
                         "omer_id")["is_returned"].transform("sum")
df["return_rate_per_cust"] = (return_rate /df["total_orders"] * 100)
# df["return_rate_per_cust"] = (
#     df.groupby("customer_id")["is_returned"].transform("mean") * 100
# )

df = pd.get_dummies(df, columns=["product_category"], prefix="product") #one hot encoding
print(df.head(20))

df["unit_price"] = (df["unit_price"] - df["unit_price"].min()) / (df["unit_price"].max() - df["unit_price"].min())
print(df["unit_price"])

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

df[["unit_price", "quantity"]] = scaler.fit_transform(df[["unit_price", "quantity"]])