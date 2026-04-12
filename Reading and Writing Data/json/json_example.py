import pandas as pd

# =====================
# READ JSON
# =====================
df = pd.read_json('data.json')

print("=== Original ===")
print(df)


# =====================
# PROCESS
# =====================
df['salary'] *= 1.1
df['age'] += 1


# =====================
# WRITE JSON
# =====================
df.to_json('output.json', orient='records', indent=2)

print("Saved output.json ")