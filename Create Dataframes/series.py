## Creating a Series
import pandas as pd

ages = pd.Series([25, 30, 35, 28], name='age')
print(ages)
# 0    25
# 1    30
# 2    35
# 3    28
# Name: age, dtype: int64

s1 = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
s2 = pd.Series([10, 20, 30], index=['B', 'C', 'D'])

print(s1 + s2)
# It matches by index labels, not position


data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['London', 'Paris', 'Berlin', 'Tokyo'],
    'salary': [50000, 62000, 58000, 71000]
}

df = pd.DataFrame(data, index=['emp_001', 'emp_002', 'emp_003', 'emp_004'])
print(df)
