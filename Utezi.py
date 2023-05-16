from bottle import *
import auth_public as auth
import numpy as np
import statistics

try:
    import psycopg2, psycopg2.extensions, psycopg2.extras
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

    conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    postgreSQL_select_Query = 'SELECT "LR" FROM "2022_kranj_10_Z" LIMIT 10'
    cur.execute(postgreSQL_select_Query)
    print("Selecting first 10 values from the column LR in 2022_kranj_10_Z table using cursor.fetchall")
    lr_values = [row[0] for row in cur.fetchall()]

    # Get the column names from the PostgreSQL schema
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='2022_kranj_10_Z' ORDER BY ordinal_position DESC LIMIT 3")
    last3_column_names = [row[0] for row in cur.fetchall()]

    # Generate the SELECT query dynamically with the last three column names
    select_last3_columns_query = 'SELECT "{}", "{}", "{}" FROM "2022_kranj_10_Z"'.format(*last3_column_names)
    cur.execute(select_last3_columns_query)
    print("Selecting the last 3 columns from the table 2022_kranj_10_Z using cursor.fetchall")
    last3_columns = cur.fetchall()

    # Extract values from the last 3 columns and convert them to seconds
    column1_values = [row[0] for row in last3_columns]
    column2_values = [row[1] for row in last3_columns]
    column3_values = [row[2] for row in last3_columns]

    time_to_seconds = lambda t: sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))
    column1_seconds = [time_to_seconds(time_str) for time_str in column1_values]
    column2_seconds = [time_to_seconds(time_str) for time_str in column2_values]
    column3_seconds = [time_to_seconds(time_str) for time_str in column3_values]


except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")

#optimalna leta
Najboljsa_leta = 2022 - np.array(lr_values)
N_L = statistics.mean(Najboljsa_leta)

#exhoustion factor
pace_column1 = np.array(column1_seconds) / 10
pace_column2 = np.array(column2_seconds) / 6.6
pace_column3 = np.array(column3_seconds) / 3.3