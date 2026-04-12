import pandas as pd

data = [
    ['Alice', 25, 'London'],
    ['Bob', 30, 'Paris'],
    ['Charlie', 35, 'Berlin']
]

df = pd.DataFrame(data, columns=['name', 'age', 'city'])
print(df)