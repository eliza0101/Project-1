# Movie Success Analysis and Prediction
#### Link to repo https://github.com/eliza0101/Project-1.git 
#### Link to presentation: https://www.canva.com/design/DAGKwzwMCek/aHYuXAeiH6sfzQCsi9eeZw/edit?utm_content=DAGKwzwMCek&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton 


## Overview
This project analyzes and predicts movie success using various datasets from Kaggle. The primary focus is on identifying trends in movie gross earnings and return on investment (ROI) to provide recommendations for future investments in the film industry.

This project aims to provide a comprehensive analysis of movie success factors using historical data. By understanding trends in gross earnings and ROI, we can make informed predictions and recommendations for future investments in the film industry.

## Datasets (Tunji)
#### File location: Movie_Datasets
We will be using the following datasets:
1. Movie Industry Dataset: Contains 6820 movies from 1986 to 2016 with attributes like budget and gross earnings. 
https://www.kaggle.com/datasets/danielgrijalvas/movies/data
2. Top 1000 Highest Grossing Movies: Lists the top 1000 highest-grossing movies. 
https://www.kaggle.com/datasets/sanjeetsinghnaik/top-1000-highest-grossing-movies
3. IMDb Movies Dataset Based on Genre: Provides a comprehensive collection of movies sorted by genre. 
https://www.kaggle.com/datasets/rajugc/imdb-movies-dataset-based-on-genre

## Naming Conventions and Data Types (Team)  
#### File location: https://docs.google.com/spreadsheets/d/1ed-JP-UDEccrv-pEuJVyn8r8lKWb5vjxwrtPR2gcMNc/edit?usp=sharing
To maintain consistency and readability, the following naming conventions and data types will be used:
* Column Naming Convention: Snake case (e.g., release_date)
* Data Types: 
    * int: For numerical values without decimals (e.g., budget, gross)
    * float: For numerical values with decimals (e.g., rating)
    * str: For categorical data (e.g., genre, director)
    * datetime: For date-related columns (e.g., release_date)

## Data Preparation (Tunji) 
#### File location: tunji finished clean.py
* Load and preprocess the datasets to ensure consistency in naming conventions and data types
* Remove duplicates and invalid information
* Handle missing values
* Merge all three datasets into one dataframe

## Dependencies
* Python
* NumPy
* Matplotlib (for visualization)
* locale
* Prophet


## Analysis Goals

### Top 10 Movies Every 5 Years (Catherine) 
#### File location: stats_data.py
**Objective:** Identify the top 10 movies every 5 years starting from the 1990s based on gross earnings.

**Purpose:** Understand what genres and types of movies were most popular among viewers over different periods.

### Genre Analysis (Catherine) 
#### File location: stats_data.py
**Objective:** From the top 10 movies identified, analyze the genres based on gross earnings.

**Purpose:** Determine which genres have consistently performed well and are preferred by viewers.

### Top 10 Movies by ROI (Eliza)
#### File location: main_movies_ey.ipynb, clean_files_ey.ipynb
**Objective:** Identify the top 10 movies in terms of ROI.

**Factors Considered:** title, ROI, gross, director, star, genre, license, year.

**Purpose:** Determine the combination of factors that contribute to the highest ROI.

## Prediction and Recommendation (Eliza)
#### File location: main_movies_ey.ipynb
Based on the analysis of the top 10 movies every five years and the top 10 movies by ROI, we will make predictions and provide recommendations for future investments in the film industry. This will help clients make informed decisions on where to invest their resources for maximum returns.