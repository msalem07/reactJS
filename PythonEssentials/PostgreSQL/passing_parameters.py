import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="Wggs8m42=")

cursor = connection.cursor()

#   Inserting into a table (num, and data are the name of the columns)
one = 8
info = "test3"

#cursor.execute("Insert INTO test (num, data) VALUES (%s,%s);", (7, "data"))
#cursor.execute("Insert Into test (num, data) VALUES (%s,%s);", (one, info))

#Look at all the changes
cursor.execute('''Select * from test;''')

print(cursor.fetchall())


#   commit the changes
connection.commit()


#   and close everything
cursor.close()
connection.close()