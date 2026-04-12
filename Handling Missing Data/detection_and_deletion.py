import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'age': [25, np.nan, 35, 28, np.nan],
    'salary': [50000, 62000, np.nan, 71000, 55000],
    'department': ['HR', 'IT', 'IT', None, 'HR']
})

print("=== Data ===\n", df)

print("\n=== isnull ===\n", df.isnull())

print("\n=== Missing per column ===\n", df.isnull().sum())

print("\n=== Total missing ===\n", df.isnull().sum().sum())

print("\n=== notnull ===\n", df.notnull())

print("Drop any null:\n", df.dropna())

print("\nDrop null in name & age:\n",
      df.dropna(subset=['name', 'age']))

print("\nDrop columns with null:\n",
      df.dropna(axis=1))

print("\nDrop fully empty rows:\n",
      df.dropna(how='all'))
# Only removes rows that are completely empty

print("\nKeep rows with >=3 values:\n",
      df.dropna(thresh=3))