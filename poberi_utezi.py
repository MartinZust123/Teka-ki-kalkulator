def fetch_utezi():
    import data.auth_public as auth
    import psycopg2
    from psycopg2 import extras

    # Connect to the database
    conn = psycopg2.connect(
        database=auth.db,
        host=auth.host,
        user=auth.user,
        password=auth.password
    )

    # Create a cursor
    cur = conn.cursor(cursor_factory=extras.DictCursor)

    # Execute a query to fetch all values from the 'utezi' table
    try:
        cur.execute("SELECT * FROM utezi")
        rows = cur.fetchall()
    except psycopg2.Error as e:
        print("Error fetching data:", e)
        rows = []

    # Close cursor and connection
    cur.close()
    conn.close()

    return rows
