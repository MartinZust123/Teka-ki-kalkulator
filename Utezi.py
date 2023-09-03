def fetch_data():
    import data.auth_public as auth
    import numpy as np
    import statistics
    try:
        import psycopg2, psycopg2.extensions, psycopg2.extras
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)

        conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)

        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        distance_columns = ['km_maraton', 'km_petintrideset', 'km_stirideset', 'km_dva', 'km_tri', 'km_tt', 'km_pet', 'km_sest', 'km_ss', 'km_deset', 'km_petnajst', 'km_sedemnajst', 'km_dvajset', 'km_enaindvajset', 'km_polmaraton', 'km_petindvajset', 'km_trideset']
        min_times_and_lrs = []

        for distance_column in distance_columns:
            postgreSQL_select_Query = f'SELECT "lr", "{distance_column}" FROM "oseba" WHERE "{distance_column}" IS NOT NULL ORDER BY "{distance_column}" LIMIT 10'
            cur.execute(postgreSQL_select_Query)
            rows = cur.fetchall()
            min_times_and_lrs.extend([(row[0], row[1], row[2], distance_column) for row in rows])

        return min_times_and_lrs  # Return the fetched data

    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # Closing database connection.
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")




