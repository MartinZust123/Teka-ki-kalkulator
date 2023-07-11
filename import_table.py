import psycopg2

try:
    conn = psycopg2.connect(database='sem2023_matejg', host='baza.fmf.uni-lj.si', user='loanns', password='n75294rw')
    conn.autocommit = True

    cur = conn.cursor()

    create_table_query = '''
        CREATE TABLE IF NOT EXISTS vsi_podatki (
            id SERIAL PRIMARY KEY,
            spol VARCHAR(255),
            priimek_ime VARCHAR(255),
            LR INTEGER,
            km2 TIME,
            km3 TIME,
            km3_3 TIME,
            km5 TIME,
            km6_6 TIME,
            km10 TIME,
            km17 TIME,
            km21 TIME,
            km21_1 TIME,
            km25 TIME,
            km30 TIME,
            km35 TIME,
            km40_1 TIME,
            km40_2 TIME,
            km42 TIME
        )
    '''
    cur.execute(create_table_query)
    print("Table 'example_table' created successfully.")

except (Exception, psycopg2.Error) as error:
    print("Error while creating table:", error)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
    print("PostgreSQL connection is closed")

