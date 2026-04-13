import pandas as pd
import numpy as np

import pandas as pd

messy_data = pd.DataFrame({
    "Name": ["  Alice ", "Bob", "CHARLIE", "alice", "David", "Bob", None],
    "Age": [25, -3, 30, 25, 200, 35, 28],
    "Email": [
        "alice@mail.com",
        "bob@",
        "charlie@mail.com",
        "alice@mail.com",
        None,
        "bob@mail.com",
        "david@mail.com"
    ],
    "Salary": ["50000", "60K", "70000", None, "80000", "60000", "55000"],
    "Date_Joined": [
        "2020-01-15",
        "2020/02/20",
        "March 3, 2020",
        "2020-01-15",
        None,
        "2020-05-10",
        "2020-06-01"
    ]
})

df = messy_data
df["Name"] = df["Name"].str.strip().str.title().fillna("Unknown")
df["Age"] = df["Age"].where((df["Age"] >= 0) & (df["Age"] <= 120), np.nan)
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].str.replace("K", "000", regex=False)
df["Salary"] = df["Salary"].str.replace(r"[^0-9]", "", regex=True)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Salary"] = df["Salary"].fillna(df["Salary"].median())
df["Date_Joined"] = pd.to_datetime(df["Date_Joined"], errors="coerce")
df = df.drop_duplicates(subset=["Name", "Email"])
print(df.duplicated(subset=["Name", "Email"]).sum())

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
df["Email_Valid"] = df["Email"].str.match(pattern)

print(df.head())