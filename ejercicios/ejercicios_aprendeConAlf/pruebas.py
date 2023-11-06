import pandas as pd

titanic = pd.read_csv('dataSets/titanic.csv', index_col=0)
print('-------------')
print(titanic['Survived'].value_counts())
print(titanic['Pclass'].value_counts())
