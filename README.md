# Project-1

# Data Analytics Project: Identifying World's Healthiest Countries

# 1. Data Import and Preparation
IMPORT WHO_World_Health_Statistics_2020_dataset
CLEAN dataset (handle missing values, remove duplicates)

# 2. Select Relevant Health Indicators
DEFINE health_indicators AS [
    "Life expectancy at birth",
    "Healthy life expectancy (HALE) at birth",
    "Mortality rate, under-5 (per 1,000 live births)",
    "Prevalence of obesity among adults",
    "Prevalence of smoking",
    "Universal health coverage (UHC) service coverage index"
]

# 3. Data Exploration
FOR EACH indicator IN health_indicators:
    CALCULATE summary statistics
    VISUALIZE distribution across countries

# 4. Create Composite Health Index
FUNCTION create_health_index(country_data):
    NORMALIZE each indicator in health_indicators
    CALCULATE weighted average of normalized indicators
    RETURN composite health index

FOR EACH country IN dataset:
    country_health_index = create_health_index(country_data)
    ADD country_health_index to country_data

# 5. Rank Countries
SORT countries by health_index in DESCENDING order
SELECT top_20_healthiest_countries

# 6. Analyze Top Performers
FOR EACH country IN top_20_healthiest_countries:
    ANALYZE performance across individual health indicators
    IDENTIFY common characteristics

# 7. Visualize Results
CREATE world map highlighting healthiest countries
CREATE bar charts for top 20 countries' health index scores
CREATE scatter plots comparing key health indicators

# 8. Statistical Analysis
PERFORM correlation analysis between health indicators
CONDUCT regression analysis to identify most influential factors

# 9. Report Generation
SUMMARIZE key findings
HIGHLIGHT top 5 healthiest countries and their characteristics
DISCUSS trends and patterns observed
PROVIDE insights on factors contributing to better health outcomes

# 10. (Optional) Predictive Modeling
IF time_permits:
    SPLIT data into training and testing sets
    TRAIN machine learning model to predict health index
    EVALUATE model performance
    IDENTIFY most important features for predicting health outcomes