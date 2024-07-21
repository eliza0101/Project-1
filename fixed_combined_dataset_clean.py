# %%
# store data set csv
Hollywood = '/Users/mac/CLASS/Project-1/clean_highest_gross_movies_df_clean..csv'
IMDb = '/Users/mac/CLASS/Project-1/clean_IMDb_movie_data.csv'

# %%
#import dependencies 
import pandas as pd
from pathlib import Path
import os

# %%
#read csv and store as df
hollywood_df = pd.read_csv(Hollywood)
IMDb_df = pd.read_csv(IMDb)

# %%
#check dataset df
hollywood_df.head(3)

# %%
#check data set df
IMDb_df.head(3)

# %%
# Combine Datasets
combined_movie_df = pd.concat([hollywood_df, IMDb_df], ignore_index=True)
combined_movie_df.head()

# %%
#check data set
combined_movie_df.info()
combined_movie_df.shape

# %%
#check for null records
combined_movie_df.isnull().mean() * 100

# %%
# Drop Null Records
combined_movie_df = combined_movie_df.fillna(0)

# %%
# Check for nulls
combined_movie_df.isnull().sum()

# %%
combined_movie_df.head(10)

# %%
sorted_df_movie = combined_movie_df.sort_values(by=['year', 'gross'], ascending=[True, False])
sorted_df_movie.head(10)

# %%
combined_movie_df.to_csv('clean_combo_movie_data.csv', index=True)

# %%
combined_movie_df.columns




# %%
combined_movie_df['gross'] = combined_movie_df['gross'].map(lambda x: '${:,.2f}'.format(x))

# %%
combined_movie_df


