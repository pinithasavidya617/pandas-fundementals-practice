import pandas as pd

df = pd.read_csv('data.csv')

print(df.query('age > 28'))

print(df.query('age > 25 and salary > 55000'))

print(df.query('city in ["London", "Tokyo"]'))

print(df.query('name.str.contains("li")', engine='python'))