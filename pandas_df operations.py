import pandas as pd

df = pd.read_csv("IMDB-Movie-Data.csv")
#print(df)

'''One way to set titles as our index is by passing the column name as an additional parameter, index_col, to the read_csv method at file load time.'''

# 1. We can set the index at load time
#movies_df_title_indexed = pd.read_csv("IMDB-Movie-Data.csv", index_col='Title')

# 2. We can set the index after the DataFrame has been created
movies_df_title_indexed = df.set_index('Title')

#print(movies_df_title_indexed)

'''We can use the head() method to visualize the first few rows of our dataset. This method outputs the first 5 rows of 
the DataFrame by default, but we can pass the number of rows we want as input parameter.'''

#print(movies_df_title_indexed.head(10))

#print(movies_df_title_indexed.tail(3))

'''info(): This method allows us to get some essential details about our dataset, like the number of rows and columns, 
the number of index entries within that index range, the type of data in each column, the number of non-null values, and 
the memory used by the DataFrame'''

#print(movies_df_title_indexed.info())

'''.shape: This is a fast and useful attribute which outputs a tuple, <rows, columns>, representing the number of rows 
and columns in the DataFrame. '''
print(movies_df_title_indexed.shape)


'''describe(): This is a great method for doing a quick analysis of the dataset. It computes summary statistics of 
integer/double variables and gives us some basic statistical details like percentiles, mean, and standard deviation'''

print(movies_df_title_indexed.describe())