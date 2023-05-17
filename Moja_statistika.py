from bottle import *
import auth_public as auth
import numpy as np
import statistics
import random
import datetime
import matplotlib.pyplot as plt
import datetime

try:
    import psycopg2, psycopg2.extensions, psycopg2.extras
    psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

    conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    postgreSQL_select_Query = 'SELECT "Rezultat" FROM "2022_kranj_10_Z" LIMIT 10'
    cur.execute(postgreSQL_select_Query)
    cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='2022_kranj_10_Z' ORDER BY ordinal_position DESC LIMIT 1")
    last_column_name = cur.fetchone()[0]

    select_last_column_query = 'SELECT "{}" FROM "2022_kranj_10_Z"'.format(last_column_name)
    cur.execute(select_last_column_query)
    last_column_values = cur.fetchall()

    column_values = [row[0] for row in last_column_values]

    time_to_seconds = lambda t: sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))
    column_seconds = [time_to_seconds(time_str) for time_str in column_values]

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")



# Exhoustion factor
pace_column = np.array(column_seconds) / 10

date_list = []
for _ in range(24):
    year = random.randint(2000, 2023)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date = datetime.date(year, month, day)
    date_list.append(date)

date_list = sorted(date_list, key=lambda date: datetime.datetime.combine(date, datetime.datetime.min.time()))

x = [date.strftime('%b %Y') for date in date_list]

plt.plot(x, pace_column)
plt.xlabel('Datum vnosa')
plt.ylabel('Tempo (sek/km)')
plt.title('Moja statistika')
plt.xticks(rotation=45)
plt.show()