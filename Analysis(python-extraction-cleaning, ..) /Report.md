# 🚗Uber Fare Analysis with Power BI


 ### 1.Introduction and Project Objective

This project presents a comprehensive data analysis of Uber fare data, designed to uncover key trends, patterns, and insights into ride-sharing dynamics. Utilizing Python for data cleaning and feature engineering, and Power BI for interactive visualization, this dashboard aims to transform raw transaction data into actionable business intelligence.

 ### The primary objectives of this project are to:
 
 <img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/39662a19-2e66-4d6c-9263-81442fbaa9a7" />
 Clean and preprocess raw Uber fare data, addressing issues such as missing values, outliers, and incorrect data types.

 <img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/cf97a88a-4bc7-41ee-a21d-411919409c4c" />
 Engineer relevant features from existing data points to enrich the analysis (e.g., hour of day, trip distance).

 <img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/8c22616d-7768-4a7e-b819-d6cc2069ebd3" />
 Develop an interactive Power BI dashboard that visualizes key metrics and trends related to Uber fares and ride volumes.

 <img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/f5f01eec-53a5-498d-ad90-0c09737330b5" />
Identify and highlight significant patterns, including temporal (hourly, daily, monthly, yearly) and geographical distributions of rides and fares.

 <img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/92396562-bb34-40d4-9940-541daab09046" />
 Provide actionable insights into peak demand periods, pricing variations, and passenger behaviors to support operational or strategic decision-making.

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

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/68a3bc30-ae96-4039-b371-0a537bfbbe08" />
hour_of_day

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/f4b094ad-e450-4514-96d8-39b0c16a8031" />
day_of_week

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/a6a6c3d3-669d-483a-9bf7-1685b51632f7" />
month

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/5e8d00c3-b92f-4fcb-8294-1d69c2176d7d" />
year

Calculation of trip_distance_km using the Haversine formula based on pickup and drop-off coordinates, providing a crucial proxy for ride duration and basis for "fare per km" analysis.

### 4.Data Analysis and Visualization (Power BI):
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/2a12fca3-844b-4361-91d9-66290ad5b80b" />
Importing the cleaned and feature-engineered dataset into Power BI Desktop.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/5786e8fa-5d2d-4e31-a123-8b04e1433643" />
Developing various interactive visualizations to explore:

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/92c46b3e-3fda-49d8-93d0-a0ba22f4b825" />
Distribution of fare_amount.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/413d2c32-9ad7-4fe1-9e0c-982d4f2b607b" />
Temporal patterns of rides and fares (hourly, daily, monthly, yearly).

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/97fb31f7-9ff4-49b3-ae40-a35a9d28f201" />
Geographic distribution of pickups.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/1653d2e7-a8a0-4020-99a8-8f9f4d34f8d1" />
Impact of passenger_count.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/5435323c-618f-4fbd-b92c-6d28c89a516d" />
Creation of custom measures (e.g., Average Fare Per Km) using DAX to derive key performance indicators.

### 5.Dashboard Creation:
<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/37bfc380-76a0-4c2f-8ccd-43becb3ea621" />
Designing a professional and interactive dashboard that consolidates all key findings.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/3586dc32-65da-4f54-92ec-2bb9951f84d9" />
Implementing slicers and drill-down capabilities for dynamic data exploration.

<img width="512" height="512" alt="image" src="https://github.com/user-attachments/assets/253ccf9e-ee9b-4b3c-b1cd-53290e511526" />
Applying consistent formatting and design principles for clarity and user-friendliness.

  
 
