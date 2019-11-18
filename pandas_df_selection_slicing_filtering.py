import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv")

'''We can extract a column by using its label (column name) and the square bracket notation:'''

'''To obtain a Series as output'''
col_as_series = movies_df['Genre']

'''Print the object type and the first 5 rows of the series'''
#print(type(col_as_series))
#print(col_as_series.head())


'''To obtain a dataFrame as output'''
col_as_df = movies_df[['Genre']]

'''Print the object type and the first 5 rows of the DF'''
#print(type(col_as_df))
#print(col_as_df.head())


'''If we want to extract multiple columns, we can simply add additional column names to the list.'''

extracted_cols = movies_df[['Genre', 'Rating', 'Revenue (Millions)']]

#print(extracted_cols.head())


'''loc: the loc attribute allows indexing and slicing that always references the explicit index, i.e., locates by name.'''

movies_df_title_indexed = movies_df.set_index('Title')
gog = movies_df_title_indexed.loc["Guardians of the Galaxy"]
#   print(gog)

'''iloc: the iloc attribute allows indexing and slicing that always references the implicit Python-style index, 
i.e., locates by numerical index. '''
gog = movies_df_title_indexed.iloc[0]
#print(gog)

'''slices with multiple rows'''
multiple_rows = movies_df_title_indexed.loc['Guardians of the Galaxy':'Sing']
#print(multiple_rows)
multiple_rows = movies_df_title_indexed.iloc[0:4]
#print(multiple_rows)

'''If we do not want to select all the columns, we can specify both rows and columns at once; the first index refers to 
rows while the second one (after the coma) to columns:'''

# Select all rows uptil 'Sing' and all columns uptil 'Director'
#print(movies_df_title_indexed.loc[:'Sing', :'Director'])
#print(movies_df_title_indexed.iloc[:4, :3])


'''# We can easily filter rows using the values of a specific row. 
# For example, for geting all our 2016 movies:'''
movies_df_title_indexed[movies_df_title_indexed['Year'] == 2016]

'''# All our movies with a rating higher than 8.0 '''
movies_df_title_indexed[movies_df_title_indexed['Rating'] > 8.0 ]

'''Say we want to retrieve the latest movies (movies released between 2010 and 2016) that had a very poor rating (score less than 6.0) 
but were among the highest earners at the box office (revenue above the 75th percentile). '''

print(movies_df_title_indexed[
    ((movies_df_title_indexed['Year'] >= 2010) & (movies_df_title_indexed['Year'] <= 2016))
    & (movies_df_title_indexed['Rating'] < 6.0)
    & (movies_df_title_indexed['Revenue (Millions)'] > movies_df_title_indexed['Revenue (Millions)'].quantile(0.75))
])
