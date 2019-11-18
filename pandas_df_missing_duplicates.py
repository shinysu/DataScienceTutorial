'''The two flavors in which we are likely to encounter missing or null values are:'''
'''None: A Python object that is often used for missing data in Python. None can only be used in arrays with data type 
‘object’ (i.e., arrays of Python objects).
NaN (Not a Number): A special floating-point value that is used to represent missing data. A floating-point type means 
that, unlike with None’s object array, we can perform mathematical operations. However, remember that, regardless of the 
operation, the result of arithmetic with NaN will be another NaN.
'''
import numpy as np
import pandas as pd

# Example with None
None_example = np.array([0, None, 2, 3])
print("dtype =", None_example.dtype)
#print(None_example)

# Example with NaN
NaN_example = np.array([0, np.nan, 2, 3])
print("dtype =", NaN_example.dtype)
#print(NaN_example)

# Math operations fail with None but give NaN as output with NaNs
#print("Arithmetic Operations")
#print("Sum with NaNs:", NaN_example.sum())
#print("Sum with None:", None_example.sum())

'''isnull() and notnull() are two useful methods for detecting null data for Pandas data structures.'''
'''isnull() returns a DataFrame where each cell is either True or False depending on that cell’s missing-value status.'''

movies_df = pd.read_csv("IMDB-Movie-Data.csv")
movies_df_title_indexed = movies_df.set_index('Title')
#print(movies_df_title_indexed.isnull())

'''We can also count the number of null values in each column using an aggregate function for summing:'''

#print(movies_df_title_indexed.isnull().sum())


'''dropna() allows us to very easily drop rows or columns. '''
'''By default, this method will drop all rows in which any null value is present and return a new DataFrame without 
altering the original one. If we want to modify our original DataFrame inplace instead, we can specify inplace=True.'''

'''Drop all rows with any missing data'''
#print(movies_df_title_indexed.dropna())

'''Drop all the columns containing any missing data'''
#print(movies_df_title_indexed.dropna(axis=1))


'''Drop columns where all the values are missing'''
movies_df.dropna(axis='columns', how='all')

'''Thresh to specify a minimum number of non-null values 
# for the row/column to be kept'''
movies_df.dropna(axis='rows', thresh=10)

''' Imputation (Filling Null Values)  '''

'''As we have just seen, dropping rows or columns with missing data can result in a losing a significant amount of interesting data. 
So often, rather than dropping data, we replace missing values with a valid value.'''

# Getting the mean value for the column:
revenue = movies_df_title_indexed['Revenue (Millions)']
revenue_mean = revenue.mean()

print("Mean Revenue:", revenue_mean)

# Let's fill the nulls with the mean value:
revenue.fillna(revenue_mean, inplace=True)

# Let's get the updated status of our DataFrame:
movies_df_title_indexed.isnull().sum()

'''Pandas allows us to very easily remove duplicates by using the drop_duplicates() method. This method returns a copy 
of the DataFrame with duplicates removed unless we choose to specify inplace=True, just like for the previously seen methods.
'''

'''Creating New Columns From Existing Columns'''

'''Say we want to introduce a new column in our DataFrame that has revenue per minute for each movie. We can divide the 
revenue by the runtime and create this new column very easily like so:'''
# We can use 'Revenue (Millions)' and 'Runtime (Minutes)' to calculate Revenue per Min for each movie:
movies_df_title_indexed['Revenue per Min'] = movies_df_title_indexed['Revenue (Millions)']/movies_df_title_indexed['Runtime (Minutes)']

movies_df_title_indexed.head()

