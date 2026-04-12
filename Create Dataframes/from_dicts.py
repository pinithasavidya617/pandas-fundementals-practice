import pandas as pd

### From a Dictionary

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'age': [25, 30, 35, 28],
    'city': ['London', 'Paris', 'Berlin', 'Tokyo'],
    'salary': [50000, 62000, 58000, 71000]
}

df = pd.DataFrame(data)
print(df)