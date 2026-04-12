import pandas as pd

df = pd.read_csv('data.csv')

print("Single column:\n", df['name'])
# df['column'] → Series (1D)

print("\nMultiple columns:\n", df[['name', 'age']])
# df[['name', 'age']]
#       name  age
# 0    Alice   25
# 1      Bob   30
# 2  Charlie   35

# Single []  → Series
# Double [[]] → DataFrame

print("\nFirst column (iloc):\n", df.iloc[:, 0])
# df.iloc[rows, columns]
# :      → all rows
# 0      → first column
# [0,2]  → column 1 and 3

print("\nFirst and third columns:\n", df.iloc[:, [0, 2]])

print("\nRow 0 (loc):\n", df.loc[0])

print("\nRows 0 to 2 (loc):\n", df.loc[0:2])

print("\nRow 0 (iloc):\n", df.iloc[0])

print("\nRows 0 to 2 (iloc):\n", df.iloc[0:2])

print("\nCell [0, 'name']:\n", df.loc[0, 'name'])
# df.iloc[0, 0]

print("\nCell [0, 0]:\n", df.iloc[0, 0])