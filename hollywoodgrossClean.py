# %%
import pandas as pd
from pathlib import Path
import os

# %%
# Store path of csv
highest_gross_movies = '/Users/mac/CLASS/Project-1/Movie_Datasets/Highest Holywood Grossing Movies.csv'

# %%
# Read csv and display in df
highest_gross_movies_df = pd.read_csv(highest_gross_movies)
highest_gross_movies_df

# %%
# Check out data
highest_gross_movies_df.info()
highest_gross_movies_df.head()
highest_gross_movies_df.describe()

# %%
#display columns
highest_gross_movies_df.columns

# %%
missing_data = highest_gross_movies_df.isnull().sum()
missing_data

# %%
#fill in data missing data
highest_gross_movies_df_clean = highest_gross_movies_df.fillna(0)
highest_gross_movies_df_clean

# %%
highest_gross_movies_df_clean['release date']= pd.to_datetime(highest_gross_movies_df_clean['Release Date'])
highest_gross_movies_df_clean.head()

# %%
highest_gross_movies_df_clean = highest_gross_movies_df_clean.rename(columns= {
    'Title' : 'title',
    'Genre' : 'genre',
    'Year' : 'year',
    'release date' : 'release_date',
    'Budget (in $)' : 'budget',
    'World Wide Sales (in $)' : 'gross',
    'Running Time' : 'runtime',
    'License' : 'license'
    
})

# %%
highest_gross_movies_df_clean.head()

# %%
highest_gross_movies_df_clean = highest_gross_movies_df_clean.drop(columns=['Release Date'])
highest_gross_movies_df_clean.head()

# %% [markdown]
# 

# %%

# Convert 'year' column to numeric (assuming it's not already numeric)
highest_gross_movies_df_clean['year'] = pd.to_numeric(highest_gross_movies_df_clean['year'], errors='coerce')

# Set 'year' as the index and sort the DataFrame by 'year' in ascending order
highest_gross_movies_df_clean = highest_gross_movies_df_clean.set_index('year').sort_index(ascending=True)

# Print the first few rows to verify the changes
highest_gross_movies_df_clean.head()

# %%
#Check data type
highest_gross_movies_df_clean.info()

# %%
columns_change= ['Domestic Opening (in $)','Domestic Sales (in $)' ,'International Sales (in $)','gross']
for column in columns_change:
    highest_gross_movies_df_clean[column] = highest_gross_movies_df_clean[column].replace('[^\d.]', '', regex=True).astype(float)


# %%


#Clean 'budget' column and convert to float
highest_gross_movies_df_clean['budget'] = highest_gross_movies_df_clean['budget'].replace('[^\d.]', '', regex=True).astype(float)

# Convert 'runtime' column to numeric (total minutes)
def convert_runtime_to_minutes(runtime_str):
    try:
        parts = runtime_str.split()
        hours = int(parts[0]) if 'hr' in parts else 0
        minutes = int(parts[2]) if 'min' in parts else 0
        total_minutes = hours * 60 + minutes
        return total_minutes
    except:
        return None

highest_gross_movies_df_clean['runtime_minutes'] = highest_gross_movies_df_clean['runtime'].apply(convert_runtime_to_minutes)

# Print DataFrame info to verify changes
highest_gross_movies_df_clean.info()
highest_gross_movies_df_clean

# %%
gross_filtered_data_90_95 = highest_gross_movies_df_clean.loc[1990:1995]
gross_filtered_data_90_95.head()

# %%
gross_filtered_data_95_00 = highest_gross_movies_df_clean.loc[1995:2000]
gross_filtered_data_95_00.head()

# %%
gross_filtered_data_00_05 = highest_gross_movies_df_clean.loc[2000:2005]
gross_filtered_data_00_05.head()

# %%
gross_filtered_data_05_10 = highest_gross_movies_df_clean.loc[2005:2010]
gross_filtered_data_05_10.head()

# %%
gross_filtered_data_10_15 = highest_gross_movies_df_clean.loc[2010:2015]
gross_filtered_data_10_15.head()

# %%
gross_filtered_data_15_20 = highest_gross_movies_df_clean.loc[2015:2020]
gross_filtered_data_15_20.head()

# %%
gross_filtered_data_20_24 = highest_gross_movies_df_clean.loc[2020:2024]
gross_filtered_data_20_24.head()


