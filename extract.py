import pandas as pd
print("extract data")
data={
    'id': [101,102,103],
    'name': ['puja','manu','siya'],
    'age': [21,22,25]
}
df=pd.DataFrame(data)
print(df)
