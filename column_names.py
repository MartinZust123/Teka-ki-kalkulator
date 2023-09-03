import psycopg2
import data.auth_public as auth

def fetch_column_names(table_name):
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(database=auth.db, host=auth.host, user=auth.user, password=auth.password)
        cur = conn.cursor()

        # Query the column names for the specified table
        query = f"SELECT column_name FROM information_schema.columns WHERE table_name = %s"
        cur.execute(query, (table_name,))
        
        # Fetch all column names into a list
        column_names = [row[0] for row in cur.fetchall()]
        
        return column_names

    except (Exception, psycopg2.Error) as error:
        print("Error fetching column names:", error)

    finally:
        # Close database connection
        if conn:
            cur.close()
            conn.close()
            print("PostgreSQL connection is closed")

# Specify the table name
table_name = "rezultat"

# Call the function to fetch column names
column_names = fetch_column_names(table_name)

# Now, 'column_names' contains a list of column names for the specified table.
print("Column names:", column_names)