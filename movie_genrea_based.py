# %%
import pandas as pd
from pathlib import Path
import os

# %%
# Directory containing all need csv files
directory = '/Users/mac/CLASS/Project-1/genre_movies'

# %%
# A list to contain all the dataframes 
dfs = []

# %%


# Loop through all the files in directory
for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(directory, filename)
        
        # Read csv file into a DataFrame
        df = pd.read_csv(filepath)
        
        # Append DF to list
        dfs.append(df)

# Concatenate all DFs into a single DF
IMDb_Movie_Dataset_df = pd.concat(dfs, ignore_index=True)

# Print combined DataFrame
IMDb_Movie_Dataset_df

# %%
#Data Inspection
IMDb_Movie_Dataset_df.info()
IMDb_Movie_Dataset_df.describe()



# %%


# Check columns
IMDb_Movie_Dataset_df.columns





# %%
# Check for missing values
missing_values = IMDb_Movie_Dataset_df.isnull().sum()
missing_values


# %%
#Fill in mixing data with 0


IMDb_Movie_Dataset_df_clean =IMDb_Movie_Dataset_df.fillna(0)

IMDb_Movie_Dataset_df_clean

# %%


# %%
#Convert year to numeric
IMDb_Movie_Dataset_df_clean['year'] = pd.to_numeric(IMDb_Movie_Dataset_df_clean['year'], errors='coerce')

# Set year as index and put in ascending order
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df_clean.set_index('year').sort_index(ascending=True)
IMDb_Movie_Dataset_df_clean



# %%
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df_clean.rename(columns= {
    'movie_name': 'title', 
    'gross(in $)': 'gross',
    'certificate': 'license'


})

IMDb_Movie_Dataset_df_clean

# %%
# Specify columns to drop as a list of column names
columns_to_drop = ['movie_id', 'director_id', 'star_id', 'description', 'votes','score','country']

# Drop specified columns from IMDb_Movie_Dataset_df
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df_clean.drop(columns=columns_to_drop)

# Print new set of columns
IMDb_Movie_Dataset_df_clean

# %%
# data types 

IMDb_Movie_Dataset_df.info()


# %%
#Convert data to the needed data types

IMDb_Movie_Dataset_df_clean['rating']= pd.to_numeric(IMDb_Movie_Dataset_df_clean['rating'], errors='coerce')
IMDb_Movie_Dataset_df_clean


# %%

# Convert 'runtime' column to numeric
IMDb_Movie_Dataset_df_clean['runtime'] = pd.to_numeric(IMDb_Movie_Dataset_df_clean['runtime'], errors='coerce')


# Print or use IMDb_Movie_Dataset_df as needed
IMDb_Movie_Dataset_df_clean

# %%

filtered_data_90_95 = IMDb_Movie_Dataset_df_clean.loc[1990:1995]
filtered_data_90_95

# %%
filtered_data_95_00 = IMDb_Movie_Dataset_df_clean.loc[1995:2000]
filtered_data_95_00

# %%
filtered_data_00_05 = IMDb_Movie_Dataset_df_clean.loc[2000:2005]
filtered_data_00_05

# %%
filtered_data_05_10 = IMDb_Movie_Dataset_df_clean.loc[2005:2010]
filtered_data_05_10

# %%
filtered_data_10_15 = IMDb_Movie_Dataset_df_clean.loc[2010:2015]
filtered_data_10_15

# %%
filtered_data_15_20 = IMDb_Movie_Dataset_df_clean.loc[2015:2020]
filtered_data_15_20

# %%
filtered_data_20_24 = IMDb_Movie_Dataset_df_clean.loc[2020:2024]
filtered_data_20_24

# %% [markdown]
# 


