''' We can create a pivot table using pivot_table; we can set index =‘Director’ (row of the pivot table) and get the
yearly revenue information by setting columns = ‘Year’:'''

import pandas as pd
movies_df = pd.read_csv("IMDB-Movie-Data.csv")
movies_df_title_indexed = movies_df.set_index('Title')

# Let's calculate the mean revenue per director but by using a pivot table instead of groupby as seen previously
print(movies_df_title_indexed.pivot_table('Revenue (Millions)', index='Director', aggfunc='sum', columns='Year').head())

'''Applying Functions'''

'''Applying functions to a dataset, apply(), is very handy for playing with data and creating new variables. To apply() 
a function means returning some value after passing each row/column of a DataFrame through some function. 
The function can be a default one or user-defined.'''

# 1. Let's define the function to put movies into buckets based on their rating
def rating_bucket(x):
    if x >= 8.0:
        return "great"
    elif x >= 7.0:
        return "good"
    elif x >= 6.0:
        return "average"
    else:
        return "bad"

# 2. Let's apply the function
movies_df_title_indexed["Rating_Category"] = movies_df_title_indexed["Rating"].apply(rating_bucket)

# 3. Let's see some results
print(movies_df_title_indexed.head(10)[['Rating','Rating_Category']])