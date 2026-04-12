import pandas as pd

df = pd.read_csv('data.csv')

print("Age > 28:\n", df[df['age'] > 28])

print("\nAge > 25 AND salary > 55000:\n",
      df[(df['age'] > 25) & (df['salary'] > 55000)])

print("\nCity in London/Tokyo:\n",
      df[df['city'].isin(['London', 'Tokyo'])])

print("\nName contains 'li':\n",
      df[df['name'].str.contains('li', case=False)])

print("\nAge between 25 and 30:\n",
      df[df['age'].between(25, 30)])

print("\nSalary not null:\n",
      df[df['salary'].notna()])