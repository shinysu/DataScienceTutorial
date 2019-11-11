import pandas as pd

series = pd.Series([4,5,6,7])
#print(series)

#print("values=", series.values)
#print("indexes=",series.index)

#print(series[2])
#print(series[1:3])

'''index need not be integers'''

data = pd.Series([12,24,36,48], index=['a','b','c','d'])

#print(data)
#print("Value at index b:",data['b'])

'''creating a series from a dictionary'''

fruits_dict = {'apples':10,'oranges':8,'bananas':3,'strawberries':20}
fruits = pd.Series(fruits_dict)
print(fruits)
print("value for apples : ",fruits['apples'])
'''series also supports slicing'''

print(fruits['oranges':'strawberries'])
