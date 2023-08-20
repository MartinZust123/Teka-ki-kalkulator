def fetch_table_data(leto,kraj,km,spol):
    import data.auth_public as auth
    import psycopg2, psycopg2.extensions, psycopg2.extras

    try:
        psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
        conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        table_name = f"{leto}_{kraj}_{km}_{spol}"
        query = f'SELECT * FROM "{table_name}";'
        cur.execute(query)
        data = cur.fetchall()

        cur.close()
        conn.close()

        return data

    except Exception as e:
        print("An error occurred:", e)

# Fetch the data from the table and store it in a variable
table_data = fetch_table_data(2022,"kranj",10,"Z")

# Print the fetched data for verification
for row in table_data:
    print(row)

