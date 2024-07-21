import pandas as pd

# List of files to be combined
uploaded_files = [
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/action.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/adventure.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/animation.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/biography.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/crime.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/family.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/fantasy.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/film-noir.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Movie_Datasets/Highest Holywood Grossing Movies.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/history.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Movie_Datasets/horror.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/movies.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/mystery.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/romance.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/scifi.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/sports.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/thriller.csv',
    '/Users/cw/Desktop/Working Class Projects/PROJECT 1/Project-1/Project-1/Project-1/genre_movies/war.csv'
]

# Read and concatenate all dataframes
dfs = []
for file in uploaded_files:
    try:
        dfs.append(pd.read_csv(file))
    except Exception as e:
        print(f"Error reading {file}: {e}")

IMDb_Movie_Dataset_df = pd.concat(dfs, ignore_index=True)

# Fill in missing data with 0
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df.fillna(0)

# Convert 'year' to numeric
IMDb_Movie_Dataset_df_clean['year'] = pd.to_numeric(IMDb_Movie_Dataset_df_clean['year'], errors='coerce')

# Rename columns
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df_clean.rename(columns= {
    'movie_name': 'title', 
    'gross(in $)': 'gross',
    'certificate': 'license'
})

# Ensure all column names are unique
def make_unique(columns):
    seen = set()
    for idx, col in enumerate(columns):
        while col in seen:
            col += '_dup'
        seen.add(col)
        columns[idx] = col
    return columns

IMDb_Movie_Dataset_df_clean.columns = make_unique(list(IMDb_Movie_Dataset_df_clean.columns))

# Drop unnecessary columns
columns_to_drop = ['movie_id', 'director_id', 'star_id', 'description', 'votes', 'Unnamed: 0', 'Title', 'Movie Info', 'Year', 'Distributor', 'Budget (in $)', 'Domestic Opening (in $)', 'Domestic Sales (in $)', 'International Sales (in $)', 'World Wide Sales (in $)', 'Release Date', 'Genre', 'Running Time', 'License']
IMDb_Movie_Dataset_df_clean = IMDb_Movie_Dataset_df_clean.drop(columns=columns_to_drop, errors='ignore')

# Convert 'rating' and 'runtime' columns to numeric
IMDb_Movie_Dataset_df_clean['rating'] = pd.to_numeric(IMDb_Movie_Dataset_df_clean['rating'], errors='coerce')
IMDb_Movie_Dataset_df_clean['runtime'] = pd.to_numeric(IMDb_Movie_Dataset_df_clean['runtime'], errors='coerce')

# Reset index to handle duplicates
IMDb_Movie_Dataset_df_clean.reset_index(drop=True, inplace=True)

# Filter the dataset starting from 1990
filtered_df = IMDb_Movie_Dataset_df_clean[IMDb_Movie_Dataset_df_clean['year'] >= 1990]

# Function to get top 10 movies based on gross earnings for a given interval
def get_top_10_movies(df, start_year, end_year):
    interval_df = df[(df['year'] >= start_year) & (df['year'] < end_year)]
    top_10 = interval_df.sort_values(by='gross', ascending=False).head(10)
    top_10['Interval'] = f"{start_year}-{end_year - 1}"
    return top_10

# List to store the top 10 movies for each 5-year interval
top_10_movies_intervals = []

# Calculate the top 10 movies for each 5-year interval from 1990
for start_year in range(1990, 2025, 5):
    end_year = start_year + 5
    top_10 = get_top_10_movies(filtered_df, start_year, end_year)
    top_10_movies_intervals.append(top_10)

# Concatenate all top 10 movies into one DataFrame
final_top_10_movies = pd.concat(top_10_movies_intervals)

# Save the final top 10 movies to a CSV file
final_top_10_movies.to_csv('/Users/cw/Desktop/top_10_movies_every_5_years.csv', index=False)

# Display the final top 10 movies DataFrame
print(final_top_10_movies)


# Analyze the genres based on gross earnings
# Split genres and explode into separate rows
final_top_10_movies['genre'] = final_top_10_movies['genre'].str.split(', ')
exploded_genres = final_top_10_movies.explode('genre')

# Group by genre and sum the gross earnings
genre_analysis = exploded_genres.groupby('genre')['gross'].sum().reset_index()

# Sort the genres by gross earnings
genre_analysis = genre_analysis.sort_values(by='gross', ascending=False)

# Save the genre analysis to a CSV file
genre_analysis.to_csv('/Users/cw/Desktop/genre_analysis_by_gross.csv', index=False)

# Display the genre analysis DataFrame
print(genre_analysis)

import matplotlib.pyplot as plt


# Calculate total gross earnings for each 5-year interval
gross_earnings_interval = final_top_10_movies.groupby('Interval')['gross'].sum().reset_index()

# Plotting the trend of gross earnings over time
plt.figure(figsize=(12, 6))
plt.plot(gross_earnings_interval['Interval'], gross_earnings_interval['gross'], marker='o')
plt.xlabel('Interval')
plt.ylabel('Total Gross Earnings')
plt.title('Total Gross Earnings for Top 10 Movies Every 5 Years')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
import seaborn as sns

# Correlation matrix
correlation_matrix = final_top_10_movies[['gross', 'rating', 'runtime']].corr()
print(correlation_matrix)

# Heatmap of the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()
