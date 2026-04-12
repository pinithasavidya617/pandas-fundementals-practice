import pandas as pd

# =========================
# READ CSV (basic)
# =========================
df = pd.read_csv('data.csv')

print("=== Full Data ===")
print(df)


# =========================
# READ with specific columns
# =========================
df_small = pd.read_csv('data.csv', usecols=['name', 'age'])

print("\n=== Selected Columns ===")
print(df_small)


# =========================
# READ only first 3 rows
# =========================
df_limited = pd.read_csv('data.csv', nrows=3)

print("\n=== First 3 Rows ===")
print(df_limited)


# =========================
# DATA PROCESSING
# =========================
df['age'] = df['age'] + 1   # increase age
df['salary'] = df['salary'] * 1.1  # increase salary by 10%

print("\n=== After Processing ===")
print(df)


# =========================
# WRITE CSV
# =========================
df.to_csv('output.csv', index=False)

print("\nSaved as output.csv ")