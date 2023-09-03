from bottle import *
import data.auth_public as auth
import psycopg2, psycopg2.extensions, psycopg2.extras
from Utezi import fetch_data

# Fetch data
min_times_and_lrs = fetch_data()

# Dictionary to store average year for each name
average_years = {}

# Dictionary to store average pace for each name
average_pace_values = {}  # Changed variable name here

# Dictionary to store distance values
distance_values = {}

for lr, min_time, divisor, distance_name in min_times_and_lrs:
    if min_time:
        # Convert datetime.time to seconds
        pace_seconds = (min_time.hour * 3600 + min_time.minute * 60 + min_time.second) / float(divisor)

        # Calculate the average year
        if distance_name in average_years:
            average_years[distance_name].append(lr)
        else:
            average_years[distance_name] = [lr]

        # Calculate the average pace
        if distance_name in average_pace_values:  # Use the correct variable name here
            average_pace_values[distance_name].append(pace_seconds)
        else:
            average_pace_values[distance_name] = [pace_seconds]

        # Store the distance value
        distance_values[distance_name] = divisor

# Calculate the average year for each name
average_year_values = {}
for distance_name, years in average_years.items():
    average_year = sum(years) / len(years)
    average_year_values[distance_name] = average_year

# Calculate the average pace for each name
average_pace_values_result = {}  # Changed variable name here
for distance_name, pace_list in average_pace_values.items():  # Use the correct variable name here
    average_pace = sum(pace_list) / len(pace_list)
    average_pace_values_result[distance_name] = average_pace

# Create a new connection to the database
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor()

# Create a new table to store data
cur.execute("""
    CREATE TABLE Utezi (
        DistanceName VARCHAR PRIMARY KEY,
        AverageYear FLOAT,
        AveragePace FLOAT,
        DistanceValue INTEGER
    )
""")

# Insert the average year, average pace, and distance value into the table
for distance_name in average_years.keys():
    cur.execute("""
        INSERT INTO Utezi (DistanceName, AverageYear, AveragePace, DistanceValue)
        VALUES (%s, %s, %s, %s)
    """, (distance_name, average_year_values.get(distance_name, None), average_pace_values_result.get(distance_name, None), distance_values.get(distance_name, None)))
    conn.commit()

# Close the database connection
cur.close()
conn.close()

