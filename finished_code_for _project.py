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


# %%
combined_movie_df.columns




# %%
# Convert 'gross' and 'budget' columns to string if they are not already
combined_movie_df['gross'] = combined_movie_df['gross'].astype(str)
combined_movie_df['budget'] = combined_movie_df['budget'].astype(str)

# Clean 'gross' and 'budget' columns: remove '$' and ','
combined_movie_df['gross'] = combined_movie_df['gross'].str.replace('[\$,]', '', regex=True)
combined_movie_df['budget'] = combined_movie_df['budget'].str.replace('[\$,]', '', regex=True)

# Convert 'gross' and 'budget' columns to numeric
combined_movie_df['gross'] = pd.to_numeric(combined_movie_df['gross'], errors='coerce')
combined_movie_df['budget'] = pd.to_numeric(combined_movie_df['budget'], errors='coerce')

# Format 'gross' and 'budget' columns back to dollars
combined_movie_df['gross'] = combined_movie_df['gross'].map(lambda x: '${:,.2f}'.format(x))
combined_movie_df['budget'] = combined_movie_df['budget'].map(lambda x: '${:,.2f}'.format(x))


# %%
#drop gross duplicate 
combined_movie_df.drop('gross.1', axis=1, inplace=True)

# %%
combined_movie_df.drop_duplicates

# %%
combined_movie_df

# %%


# %%
#1990-1995 DATA
filtered_data_90_95 = combined_movie_df.loc[1990:1995]
filtered_data_90_95

# %%
filtered_data_95_00 = combined_movie_df.loc[1995:2000]
filtered_data_95_00

# %%
import pandas as pd

# Assuming combined_movie_df is your DataFrame with movie data
# Example dataset (replace with your actual data)

# Step 1: Convert 'gross' column to numeric
combined_movie_df['gross'] = combined_movie_df['gross'].str.replace('[\$,]', '', regex=True).astype(float)


# Step 1: Filter data from 1990 to 2024
filtered_data = combined_movie_df[(combined_movie_df['year'] >= 1990) & (combined_movie_df['year'] <= 2024)]

# Step 2: Group by 5-year periods
groups = filtered_data.groupby((filtered_data['year'] // 5) * 5)

# Step 3: Find top 10 movies in gross profit for each 5-year period
top_10_movies = []
for name, group in groups:
    top_10 = group.nlargest(10, 'gross')  # Select top 10 movies by gross profit
    top_10_movies.append(top_10)

# Step 4: Concatenate results into a single DataFrame (optional)
top_10_movies_df = pd.concat(top_10_movies)

# Display or further process top_10_movies_df
print(top_10_movies_df)


# %%
filtered_data_1 = combined_movie_df[(combined_movie_df['year'] >= 1990) & (combined_movie_df['year'] <= 1995)]
filtered_data_1.head()

# %%
#DISPLAY top 10 gross movies 1990 -2000
# Ensure 'gross' column is already in numeric format (float)
combined_movie_df['gross'] = combined_movie_df['gross'].astype(float)

# Filter the DataFrame for movies released between 1990 and 1995
filtered_data_1 = combined_movie_df[(combined_movie_df['year'] >= 1990) & (combined_movie_df['year'] <= 2000)]

# Sort by 'gross' in descending order and select top 10 movies
top_10_movies = filtered_data_1.nlargest(10, 'gross')

# Make a copy to preserve original DataFrame and format 'gross' in millions with a dollar sign
top_10_movies_with_dollar = top_10_movies.copy()
top_10_movies_with_dollar['gross'] = top_10_movies_with_dollar['gross'].map(lambda x: '${:,.2f}M'.format(x / 1000000))

# Extract the required columns for display
top_10_movies_display_90_00 = top_10_movies_with_dollar[['title', 'year', 'gross','genre']]

# Display the top 10 movies based on gross profit in the specified time frame
top_10_movies_display_90_00


# %%
#DISPLAY top 10 gross movies 2000-2010
# Ensure 'gross' column is already in numeric format (float)
combined_movie_df['gross'] = combined_movie_df['gross'].astype(float)

# Filter the DataFrame for movies released between 1990 and 1995
filtered_data_1 = combined_movie_df[(combined_movie_df['year'] >= 2000) & (combined_movie_df['year'] <= 2010)]

# Sort by 'gross' in descending order and select top 10 movies
top_10_movies = filtered_data_1.nlargest(10, 'gross')

# Make a copy to preserve original DataFrame and format 'gross' in millions with a dollar sign
top_10_movies_with_dollar = top_10_movies.copy()
top_10_movies_with_dollar['gross'] = top_10_movies_with_dollar['gross'].map(lambda x: '${:,.2f}M'.format(x / 1000000))

# Extract the required columns for display
top_10_movies_display_00_10 = top_10_movies_with_dollar[['title', 'year', 'gross','genre']]

# Display the top 10 movies based on gross profit in the specified time frame
top_10_movies_display_00_10

# %%
#DISPLAY top 10 gross movies 2010-2020
# Ensure 'gross' column is already in numeric format (float)
combined_movie_df['gross'] = combined_movie_df['gross'].astype(float)

# Filter the DataFrame for movies released between 1990 and 1995
filtered_data_1 = combined_movie_df[(combined_movie_df['year'] >= 2010) & (combined_movie_df['year'] <= 2020)]

# Sort by 'gross' in descending order and select top 10 movies
top_10_movies = filtered_data_1.nlargest(10, 'gross')

# Make a copy to preserve original DataFrame and format 'gross' in millions with a dollar sign
top_10_movies_with_dollar = top_10_movies.copy()
top_10_movies_with_dollar['gross'] = top_10_movies_with_dollar['gross'].map(lambda x: '${:,.2f}M'.format(x / 1000000))

# Extract the required columns for display
top_10_movies_display_10_20 = top_10_movies_with_dollar[['title', 'year', 'gross','genre']]

# Display the top 10 movies based on gross profit in the specified time frame
top_10_movies_display_10_20

# %%


# %%



top_10_movies['gross_millions'] = top_10_movies['gross'] / 1000000

# Plotting the top 10 movies by gross profit with movie name, year, and in millions
plt.figure(figsize=(12, 8))
bars = plt.bar([f'{movie}\n({year})' for movie, year in zip(top_10_movies['title'], top_10_movies['year'])], top_10_movies['gross_millions'], color='blue')
plt.xlabel('Movie Name (Year)')
plt.ylabel('Gross Profit (Millions $)')
plt.title('Top 10 Movies by Gross Profit')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.1f}', ha='center', va='bottom', fontsize=8)

plt.show()


# %%
import pandas as pd
import matplotlib.pyplot as plt


# Sort by 'gross' in descending order and select top 10 movies
top_10_movies = combined_movie_df.nlargest(10, 'gross')



# Plotting the top 10 movies by budget with movie name, year, and in millions
plt.figure(figsize=(12, 8))
bars = plt.bar([f'{movie}\n({year})' for movie, year in zip(top_10_movies['title'], top_10_movies['year'])], top_10_movies['budget'], color='green')
plt.xlabel('Movie Name (Year)')
plt.ylabel('Budget ( $)')
plt.title('Top 10 Movies by Budget')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Add value labels on top of each bar
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.1f}', ha='center', va='bottom', fontsize=8)

plt.show()


# %%

top_10_movies['gross'] = top_10_movies['gross'].apply(lambda x: '{:,.0f}'.format(x))

# %%
scope_top_10_movies = top_10_movies[['gross','star','director','title','genre','year']]
scope_top_10_movies


