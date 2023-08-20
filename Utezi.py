def fetch_data():
    import data.auth_public as auth
    import numpy as np
    import statistics
    try:
        import psycopg2, psycopg2.extensions, psycopg2.extras
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

        conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        distance_columns = ["3.3km", "6.6km", "10km", "3km", "6km", "17km", "21km", "5km", "15km", "20km", "21.1km", "25km", "30km", "35km", "40km", "42km", "2km"]
        min_times_and_lrs = []

        for distance_column in distance_columns:
            postgreSQL_select_Query = f'SELECT "lr", "{distance_column}" FROM "oseba" WHERE "{distance_column}" IS NOT NULL ORDER BY "{distance_column}" LIMIT 10'
            cur.execute(postgreSQL_select_Query)
            rows = cur.fetchall()
            min_times_and_lrs.extend([(row[0], row[1], distance_column) for row in rows])

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

    return 


