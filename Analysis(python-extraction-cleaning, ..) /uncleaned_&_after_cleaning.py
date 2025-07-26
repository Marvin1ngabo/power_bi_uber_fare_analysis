import pandas as pd
import numpy as np

# --- Load the CLEANED dataset (essential for feature engineering) ---
# Make sure 'uber_fares_cleaned.csv' is in the same directory as this script,
# or provide the full path to it.
try:
    df = pd.read_csv('uber_fares_cleaned.csv')
    print("Cleaned dataset 'uber_fares_cleaned.csv' loaded successfully for feature engineering.")
except FileNotFoundError:
    print("Error: 'uber_fares_cleaned.csv' not found. Please ensure the path is correct.")
    print("You need to run the full cleaning script once to generate this file first.")
    # You might want to exit here if the file is truly missing
    exit()

# Ensure 'pickup_datetime' is a datetime object
df['pickup_datetime'] = pd.to_datetime(df['pickup_datetime'], utc=True, errors='coerce')

# --- 3.a. Create New Features ---
print("\n--- Starting Feature Engineering ---")

# Haversine distance function (make sure this is defined)
def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371
    lat1_rad = np.radians(lat1)
    lon1_rad = np.radians(lon1)
    lat2_rad = np.radians(lat2)
    lon2_rad = np.radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = np.sin(dlat / 2)**2 + np.cos(lat1_rad) * np.cos(lat2_rad) * np.sin(dlon / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    distance = R * c
    return distance

# Calculate trip_distance_km
df['trip_distance_km'] = df.apply(
    lambda row: haversine_distance(
        row['pickup_latitude'], row['pickup_longitude'],
        row['dropoff_latitude'], row['dropoff_longitude']
    ),
    axis=1
)
print("Created 'trip_distance_km' feature.")

# --- THIS IS THE CRUCIAL PART FOR 'hour_of_day' ---
df['hour_of_day'] = df['pickup_datetime'].dt.hour
df['day_of_week'] = df['pickup_datetime'].dt.day_name()
df['month'] = df['pickup_datetime'].dt.month
df['year'] = df['pickup_datetime'].dt.year
print("Created 'hour_of_day', 'day_of_week', 'month' and 'year' features.")

print("\n--- Feature Engineering Complete ---")

# --- Export the DataFrame WITH NEW FEATURES ---
output_file_path_with_features = 'uber_fares_cleaned_with_features.csv'
df.to_csv(output_file_path_with_features, index=False)
print(f"\nCleaned dataset with new features exported to: {output_file_path_with_features}")
