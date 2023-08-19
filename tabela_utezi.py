from bottle import *
import data.auth_public as auth
import psycopg2, psycopg2.extensions, psycopg2.extras
from Utezi import fetch_data

min_times_and_lrs = fetch_data()
pace_averages = {}  # Dictionary to store average pace for each column
for lr, min_time, column_name in min_times_and_lrs:
    if min_time:
        pace_seconds = (min_time.hour * 3600 + min_time.minute * 60 + min_time.second) / float(column_name[:-2])
        if column_name in pace_averages:
            pace_averages[column_name].append(pace_seconds)
        else:
            pace_averages[column_name] = [pace_seconds]

average_paces = {}  # Dictionary to store average pace for each column
for column_name, pace_list in pace_averages.items():
    average_pace = sum(pace_list) / len(pace_list)
    average_paces[column_name] = average_pace

print("Average paces:", average_paces)

# Calculate opt_leta and save it to the SQL table
valid_lrs = [row[0] for row in min_times_and_lrs if row[0] is not None]
average_lr = sum(valid_lrs) / len(valid_lrs)
opt_leta = average_lr  # Save the average LR value to opt_leta

# Create a new connection to the database
conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
cur = conn.cursor()

# Create a new table to store average paces and opt_leta
cur.execute("""
    CREATE TABLE Utezi (
        DistanceColumn VARCHAR PRIMARY KEY,
        AveragePace FLOAT,
        OptLeta FLOAT
    )
""")

# Insert the average pace values and opt_leta into the table
for column_name, average_pace in average_paces.items():
    cur.execute("""
        INSERT INTO Utezi (DistanceColumn, AveragePace, OptLeta)
        VALUES (%s, %s, %s)
    """, (column_name, average_pace, opt_leta))

# Commit the changes and close the connection
conn.commit()
cur.close()
conn.close()