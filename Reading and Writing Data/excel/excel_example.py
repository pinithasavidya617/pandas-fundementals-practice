import pandas as pd

# =====================
# READ EXCEL
# =====================
df = pd.read_excel('data.xlsx', sheet_name='Sheet1')

print("=== Original Data ===")
print(df)


# =====================
# PROCESS DATA
# =====================
df['age'] += 1
df['salary'] *= 1.1


# =====================
# WRITE EXCEL
# =====================
df.to_excel('output.xlsx', index=False, sheet_name='Results')

print("Saved to output.xlsx ")