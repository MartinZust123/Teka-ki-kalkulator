from bottle import *
import data.auth_public as auth
import psycopg2, psycopg2.extensions, psycopg2.extras
from Utezi import fetch_data

# poberi podatki
min_times_and_lrs = fetch_data()

average_years = {}

average_pace_values = {} 

distance_values = {}

for lr, min_time, divisor, distance_name in min_times_and_lrs:
    if min_time:
        # Spremeni v sekunde
        pace_seconds = (min_time.hour * 3600 + min_time.minute * 60 + min_time.second) / float(divisor)

        # Povprečno leto
        if distance_name in average_years:
            average_years[distance_name].append(lr)
        else:
            average_years[distance_name] = [lr]

        # Povprečen pace
        if distance_name in average_pace_values:
            average_pace_values[distance_name].append(pace_seconds)
        else:
            average_pace_values[distance_name] = [pace_seconds]

        distance_values[distance_name] = divisor

# Povprečno leto
average_year_values = {}
for distance_name, years in average_years.items():
    average_year = sum(years) / len(years)
    average_year_values[distance_name] = average_year

# Povprečni pace za maraton
average_pace_values_result = {} 
for distance_name, pace_list in average_pace_values.items(): 
    average_pace = sum(pace_list) / len(pace_list)
    average_pace_values_result[distance_name] = average_pace

conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor()

# Ustvari tabelo
cur.execute("""
    CREATE TABLE Utezi (
        DistanceName VARCHAR PRIMARY KEY,
        AverageYear FLOAT,
        AveragePace FLOAT,
        DistanceValue INTEGER
    )
""")

# Vstavi podatke v tabelo
for distance_name in average_years.keys():
    cur.execute("""
        INSERT INTO Utezi (DistanceName, AverageYear, AveragePace, DistanceValue)
        VALUES (%s, %s, %s, %s)
    """, (distance_name, average_year_values.get(distance_name, None), average_pace_values_result.get(distance_name, None), distance_values.get(distance_name, None)))
    conn.commit()

cur.close()
conn.close()

