import pandas as pd
from sqlalchemy import create_engine

# =========================
# CREATE ENGINE (database)
# =========================
engine = create_engine('sqlite:///database.db')


# =========================
# CREATE SAMPLE DATA
# =========================
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['London', 'Paris', 'Berlin', 'Tokyo']
}

df = pd.DataFrame(data)


# =========================
# WRITE TO DATABASE
# =========================
df.to_sql('users', engine, if_exists='replace', index=False)

print("Data written to database ")


# =========================
# READ FROM DATABASE
# =========================
df_read = pd.read_sql('SELECT * FROM users', engine)

print("\n=== Data from DB ===")
print(df_read)

print("\n=== Filtered Data from DB ===")
df_read = pd.read_sql('SELECT * FROM users WHERE age > 28', engine)
print(df_read)