# Import dependencies 
import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
from prophet import Prophet
from pytrends.request import TrendReq 

# Load the datasets 
amazon_skincare = pd.read_csv('amazon_skincare_products.csv')
amazon_ratings = pd.read_csv('amazon_ratings_beauty_products.csv')
cosmetic_brands = pd.read_csv('cosmetic_brand_products.csv')

# Data cleaning (Richard)
def clean_data(df):
    # Remove duplicate rows

    # Handle missing values

    # Convert price to numeric, removing currency symbol

    # Convert rating to numeric

    # Extract number of reviews and convert to numeric

    # Convert date to datetime

# Clean the data (Richard)

# Fetch Google Trends data (Richard)

# Get trends for popular skincare products - identify and visualize the top 10 products by the number of reviews. (Catherine)

# Customer preferences - identify and visualize the top 10 highly rated skincare products. (Catherine)

# Market trends - visualize Google Trends data to show the relative search interest for the specified skincare products over time. (Catherine)

# Competitive Pricing - analyzes and visualize the average price by brand. (Tunji)

# Analyze price distribution - visualize the distribution of product prices. (Tunji)

# Analyze rating distribution - visualize the distribution of product ratings. (Tunji)

# Correlation between price and rating - visualize the correlation between product price and rating using a scatter plot. (Tunji)

# Time Series Forecasting with Prophet (Eliza)
# Prepare the data for Prophet by aggregating the number of reviews by date.
# Fit the Prophet model to the time series data.

# Make future predictions and visualizes the forecast and its components. (Eliza)

# Recommend top 3 products based on high ratings (≥4.5) and a large number of reviews (>1000). (Eliza)

# Print top 3 recommended skincare products. (Eliza)