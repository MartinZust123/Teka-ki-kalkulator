import psycopg2
import psycopg2.extensions
import psycopg2.extras
import auth_public as auth

try:
    conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
    conn.autocommit = True
    cur = conn.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS moji_podatki (
            Leta VARCHAR(255),
            Tempo VARCHAR(255),
            Razdalja VARCHAR(255),
            Cas VARCHAR(255)
        )
    '''
    cur.execute(create_table_query)
    conn.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while creating table:", error)

finally:
    # closing database connection.
    if conn:
        cur.close()
        conn.close()
        print("PostgreSQL connection is closed")