import pandas as pd

movies_df = pd.read_csv("IMDB-Movie-Data.csv")

'''Let’s group our dataset by director and see how much revenue each director has'''
#print(movies_df.groupby('Director').sum())

'''Let’s group our dataset by director and see the average rating of each director'''
#print(movies_df.groupby('Director')[['Rating']].mean())

'''Let’s group our dataset by director and see who earned the most'''
#print(movies_df.groupby('Director')[['Revenue (Millions)']].sum().sort_values(['Revenue (Millions)'], ascending=False))

movies_df_title_indexed = movies_df.set_index('Title')
data_sorted = movies_df_title_indexed.sort_values(['Revenue (Millions)','Rating'], ascending=False)
print(data_sorted[['Revenue (Millions)','Rating']].head(10))
