import pandas as pd

'''Constructing a DataFrame From a Series Object'''

data = pd.Series([12,24,36,48], index=['apples','bananas','oranges','strawberries'])
dataframe1 = pd.DataFrame(data,columns=['quantity'])
#print(dataframe1)

'''Constructing a DataFrame From a Dictionary'''

dict1 = {"country":['Norway','sweden','Spain', 'France'],
         "capital":["Oslo", "Stockholm", "Madrid", "Paris"],
         "SomeColumn": ["100", "200", "300", "400"]}

data1 = pd.DataFrame(dict1)
#print(data1)

'''construct a DataFrame from a dictionary of Series objects.'''

price = pd.Series([4, 4.5, 8, 7.5], index=['apples','bananas','oranges','strawberries'])
df = pd.DataFrame({'quantity':data, 'price':price})
print(df)

'''Constructing a Dataframe by Importing Data From a File'''

df = pd.read_csv('data1.csv')
df = pd.read_json('data2.json')