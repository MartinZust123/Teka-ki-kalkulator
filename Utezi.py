def fetch_data():
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
        lr_values = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='2022_kranj_10_Z' ORDER BY ordinal_position DESC LIMIT 1")
        last_column_name = cur.fetchone()[0]

        select_last_column_query = 'SELECT "{}" FROM "2022_kranj_10_Z"'.format(last_column_name)
        cur.execute(select_last_column_query)
        last_column_values = cur.fetchall()

        column_values = [row[0] for row in last_column_values]

        time_to_seconds = lambda t: sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))
        column_seconds = [time_to_seconds(time_str) for time_str in column_values]

        cur.execute("SELECT column_name FROM information_schema.columns WHERE table_name='2022_kranj_10_Z' ORDER BY ordinal_position LIMIT 6 OFFSET 5")
        sixth_column_name = cur.fetchone()[0]

        select_sixth_column_query = 'SELECT "{}" FROM "2022_kranj_10_Z"'.format(sixth_column_name)
        cur.execute(select_sixth_column_query)
        sixth_column_values = cur.fetchall()

        column_values_2 = [row[0] for row in sixth_column_values]

        time_to_seconds_2 = lambda t: sum(int(x) * 60 ** i for i, x in enumerate(reversed(t.split(':'))))
        column_seconds_2 = [time_to_seconds_2(time_str) for time_str in column_values_2]


    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

    # Optimalna leta
    Najboljsa_leta = 2022 - np.array(lr_values)
    N_L = statistics.mean(Najboljsa_leta)

    # Exhoustion factor
    pace_column = np.array(column_seconds) / 10
    pace_column_2 = np.array(column_seconds_2) / 3.3
    exhoustion_factor = statistics.mean(pace_column/pace_column_2)

    return N_L, exhoustion_factor