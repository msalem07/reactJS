import psycopg2

# Connect to an existing database
conn = psycopg2.connect(database="postgres", user="postgres", password="Wggs8m42=")

# Open a cursor to perform database operations
cur = conn.cursor()

#Execute commands
#cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")

#cur.execute("INSERT INTO test (num, data) VALUES(%s, %s)",(100,"abc'def"))

cur.execute("SELECT * FROM cars;")

#Fetch the next row, the next set of rows, or all rows, returning them as a list of tuples
data = cur.fetchone()
#cur.fetchmany(2)
#cur.fetchmany(10)
#cur.fetchall()
print(data)

#Make the changes to the database persistent
conn.commit()


#close the communication with the database
cur.close()
conn.close()
