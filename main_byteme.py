"""Project 1: Byteme
   Instructor: Eric Cadena
   Team Members: Eliza Young, Tunji Air, Catherine Wanko, Richard M. Okhai"""


# Import dependencies 
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
#from prophet import Prophet
#from pytrends.request import TrendReq 

# Load the datasets 
amazon_skincare = pd.read_csv("./Resources/amazon_skincare_products.csv")
amazon_ratings = pd.read_csv("./Resources/amazon_ratings_beauty_products.csv")
cosmetic_brands = pd.read_csv("./Resources/cosmetic_brand_products.csv")


# Data cleaning 
def clean_data(amazon_skin, amazon_r, cosmetic_brd):
    # Remove duplicate rows - Amazon Skincare
    amazon_skin = amazon_skin.applymap(lambda x: str(x) if isinstance(x, list) else x)
    amazon_skin = amazon_skin.drop_duplicates().reset_index(drop=True)

    #Remove duplicate rows - Amazon Rating
    amazon_r = amazon_r.applymap(lambda x: str(x) if isinstance(x, list) else x)
    amazon_r = amazon_r.drop_duplicates().reset_index(drop=True)

    #Remove duplicate rows - Cosmetic Brands
    cosmetic_brd = cosmetic_brd.applymap(lambda x: str(x) if isinstance(x, list) else x)
    cosmetic_brd = cosmetic_brd.drop_duplicates().reset_index(drop=True)


    # Handle missing values - Amazon Skincare
    #forward fill argu
    amazon_skin.fillna(method='ffill', inplace=True)
    amazon_r.fillna(method='ffill', inplace=True)

    #although cosmetic df does not contain any null or empyty value
    cosmetic_brd.fillna(method='ffill', inplace=True)


    # Convert price on rating/skincare dataset to float since it contains a decimal
    # removing currency symbol
    amazon_skin['Price'] = amazon_skin['Price'].astype(float)
    amazon_r['price'] = amazon_r['price'].astype(float)


    #drop price_sign on rating df since it only contains the $ symbol, 
    # but currency table still exist
    amazon_r.drop(columns=["price_sign"], inplace=True)

    # Extract number of reviews and convert to 
    # float since it might contain decis on rating dataset
    #utilize str.extract exprsn to retract num digits
    amazon_r['rating'] = amazon_r['rating'].str.extract('(\d+)').astype(float)

    #utilize str.extract exprsn to retract num digits
    cosmetic_brd['Rating'] = cosmetic_brd['Rating'].str.extract('(\d+)').astype(float)

    # Convert date to datetime - created_at, updated_at (a-rating)
    amazon_r['created_at', 'updated_at'] = pd.to_datetime(amazon_r['created_at', 'updated_at'])

    # convert date to datetime on cosmetic brand 
    # and check for invalid parsing to be conv to NaaN
    cosmetic_brd['Timestamp'] = pd.to_datetime(cosmetic_brd['Timestamp'])


# Clean the data?
    return amazon_skin, amazon_r, cosmetic_brd



# Fetch Google Trends data 

# Get trends for popular skincare products - identify and visualize the top 10 products by the number of reviews.


# Customer preferences - identify and visualize the top 10 highly rated skincare products.


# Market trends - visualize Google Trends data to show the relative search interest for the specified skincare products over time.

# Competitive Pricing - analyzes and visualize the average price by brand.

# Analyze price distribution - visualize the distribution of product prices.


# Analyze rating distribution - visualize the distribution of product ratings.


# Correlation between price and rating - visualize the correlation between product price and rating using a scatter plot.


# Time Series Forecasting with Prophet
# Prepare the data for Prophet by aggregating the number of reviews by date.
# Fit the Prophet model to the time series data.



# Make future predictions and visualizes the forecast and its components.


# Recommend top 3 products based on high ratings (≥4.5) and a large number of reviews (>1000).

# Print top 3 recommended skincare products