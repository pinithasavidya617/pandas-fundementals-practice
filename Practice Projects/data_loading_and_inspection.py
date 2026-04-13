import pandas as pd
import seaborn as sns

df = sns.load_dataset("titanic")
print("First 10 rows", df.head(10))
print(f"Shape : {df.shape}")
print(f"Data types {df.dtypes}")
print(f"Memory Usage {df.memory_usage()}")
print(df.describe(include='all'))
print(f"Missing values : {df.isnull().sum()}")
print(f"Missing values percentage : {(df.isnull().sum() / len(df)) * 100}%")
