# 🚗Uber Fare Analysis with Power BI


 ### 1.Introduction and Project Objective

This project presents a comprehensive data analysis of Uber fare data, designed to uncover key trends, patterns, and insights into ride-sharing dynamics. Utilizing Python for data cleaning and feature engineering, and Power BI for interactive visualization, this dashboard aims to transform raw transaction data into actionable business intelligence.

 ### The primary objectives of this project are to:
 
 ✅Clean and preprocess raw Uber fare data, addressing issues such as missing values, outliers, and incorrect data types.

 ✅Engineer relevant features from existing data points to enrich the analysis (e.g., hour of day, trip distance).

 ✅Develop an interactive Power BI dashboard that visualizes key metrics and trends related to Uber fares and ride volumes.

 ✅Identify and highlight significant patterns, including temporal (hourly, daily, monthly, yearly) and geographical distributions of rides and fares.

 ✅Provide actionable insights into peak demand periods, pricing variations, and passenger behaviors to support operational or strategic decision-making.

 ### 2.Methodology: Data Collection and Analysis Approach

 This project followed a structured analytical approach, moving from raw data acquisition and preprocessing to advanced feature engineering and interactive dashboard   creation.
 ### 2.1.Data Collection
 
 The dataset utilized for this analysis is the "New York City Taxi Fare Prediction" dataset (often used for Uber fare analysis due to its similar structure), publicly available on Kaggle. This dataset contains historical trip records, including fare amounts, pickup and drop-off locations, timestamps, and passenger counts.

### 2.2.Tools and Technologies
 The analysis was conducted using a combination of powerful data science tools:

Python: Employed for robust data cleaning, preprocessing, and feature engineering, leveraging libraries such as:

  ###### pandas for data manipulation and analysis.

  ###### numpy for numerical operations.

  ######  scikit-learn (though less explicitly used for modeling, its principles for data prep might apply).

  ######  matplotlib and seaborn for initial exploratory data analysis (EDA) visualizations.

  ######  Power BI Desktop: Utilized for creating an interactive and visually compelling dashboard, enabling dynamic exploration of the data.

### 2.3.Analysis Workflow  
  The project's analytical workflow was divided into the following key phases:

  #### 1. Data Understanding and Initial Assessment:
  Initial loading of the dataset.
  Examination of data types, summary statistics, and early identification of missing values or obvious inconsistencies.

  #### 2. Data Cleaning and Preprocessing (Python):
  Handling of missing values (e.g., rows with NaNs in critical columns were removed).
  Data type conversion (e.g., fare_amount to numeric, pickup_datetime to datetime objects).
  Outlier detection and removal for key numerical fields, including:
  fare_amount: Filtering out values less than zero or excessively high.
  passenger_count: Removing records with zero passengers or an unrealistically high number.
  Geographical Coordinates: Filtering out invalid latitude and longitude values (e.g., outside standard ranges or at (0,0)).

### 3.Feature Engineering (Python):
Creation of new, insightful features derived from pickup_datetime to capture temporal patterns:

✅hour_of_day

✅day_of_week

✅month

✅year

Calculation of trip_distance_km using the Haversine formula based on pickup and drop-off coordinates, providing a crucial proxy for ride duration and basis for "fare per km" analysis.

### 4.Data Analysis and Visualization (Power BI):
Importing the cleaned and feature-engineered dataset into Power BI Desktop.

Developing various interactive visualizations to explore:

Distribution of fare_amount.

Temporal patterns of rides and fares (hourly, daily, monthly, yearly).

Geographic distribution of pickups.

Impact of passenger_count.

Creation of custom measures (e.g., Average Fare Per Km) using DAX to derive key performance indicators.

### 5.Dashboard Creation:

Designing a professional and interactive dashboard that consolidates all key findings.

Implementing slicers and drill-down capabilities for dynamic data exploration.

Applying consistent formatting and design principles for clarity and user-friendliness.

  
 
