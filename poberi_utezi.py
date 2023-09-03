def fetch_utezi():
    import data.auth_public as auth
    import psycopg2
    from psycopg2 import extras

    # Povezi na bazo
    conn = psycopg2.connect(
        database=auth.db,
        host=auth.host,
        user=auth.user,
        password=auth.password
    )

    cur = conn.cursor(cursor_factory=extras.DictCursor)

    # Poberi utezi
    try:
        cur.execute("SELECT * FROM utezi")
        rows = cur.fetchall()
    except psycopg2.Error as e:
        print("Error fetching data:", e)
        rows = []

    cur.close()
    conn.close()

    return rows
