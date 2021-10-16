import pandas as pd

data = pd.read_csv('./HTML_to_CSV.csv')
print(data.shape)
# print(data.head())
print(data.to_string(index=False))