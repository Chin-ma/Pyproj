import pandas as pd

data = pd.read_csv('innovators.csv')
print('Shape: ',data.shape)
print('\nFeatures: ',data.columns)

x = data[data.columns[:-1]]
y = data[data.columns[-1]]

print("\nFeature matrix: \n",x.head())
print("\nResponse vector: \n",y.head())