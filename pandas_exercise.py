'''Q1'''

import pandas as pd

# Input
data = {'Artist': ['Ariana Grande', 'Taylor Swift', 'Ed Sheeran', 'Justin Bieber', 'Lady Gaga', 'Bruno Mars'],
        'Genre': ['Jazz', 'Rock', 'Jazz', 'Pop', 'Pop', 'Rock'],
        'Listeners': [1300000, 2700000, 5000000, 2000000, 3000000, 1100000]}

labels = ['AG', 'TS', 'ED', 'JB', 'LG', 'BM']

'''Q1. Create a DataFrame from the given dictionary data and index labels and store it in the variable called “df”.'''

df = pd.DataFrame(data,index=labels)

'''Select the column labelled “Listeners” and store it in the variable called “col”. b) Select the first row and store 
it in the variable called “row”.'''
col = df['Listeners']
row = df.iloc[0]
print("Row:", row)
print("Col:", col)

'''Q3. Select all the rows where the Genre is ‘Pop’ and store the result in the variable “pop_artists”.'''

pop_artists = df[df['Genre'] == 'Pop']
print(pop_artists)

'''Q4. Select the artists who have more than 2,000,000 listeners and whose Genre is ‘Pop’ and save the output in the 
variable called “top_pop”.'''

top_pop = df[(df['Genre'] == "Pop") & (df['Listeners'] > 2000000) ]

'''Q5. Perform a grouping by Genre using sum() as the aggregation function and store the results in the variable called “grouped”.'''

grouped = df.groupby('Genre').sum()