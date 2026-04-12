import pandas as pd
import numpy as np

df = pd.DataFrame({
    'name': ['Alice', 'Bob', None, 'Diana', 'Eve'],
    'age': [25, np.nan, 35, 28, np.nan],
    'salary': [50000, 62000, np.nan, 71000, 55000],
    'department': ['HR', 'IT', 'IT', None, 'HR']
})

# Fill operations
df['department'] = df['department'].fillna('Unknown')
# None → "Unknown"
df['age'] = df['age'].fillna(df['age'].mean())
df['salary'] = df['salary'].fillna(df['salary'].median())

df['salary'].interpolate() #Fill missing values based on trend
# Indicator
df['age_was_missing'] = df['age'].isnull().astype(int)

print(df)

# | Method | Use when            |
# | ------ | ------------------- |
# | Mean   | Data is normal      |
# | Median | Data has outliers   |

df['age'].ffill()
# Use previous row value : 25, NaN → becomes 25
df['age'].bfill()
# Use next row value : NaN, 35 → becomes 35
df.fillna({
    'age': df['age'].median(),
    'department': 'Unknown'
})
# Fill Multiple Columns


# | Situation   | Method                 |
# | ----------- | ---------------------- |
# | Few missing | dropna()               |
# | Numeric     | mean / median          |
# | Categorical | "Unknown"              |
# | Time series | ffill / interpolate    |
# | ML models   | + missing indicator    |
