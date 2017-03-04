import psycopg2
import re

CARS = psycopg2.extensions.new_type((16408,), 'CARS", cast_car')
psycopg2.extensions.register_type(CARS)

class Car:

    def __init__(self):
        self.car_type = ''
        self.car_model = ''


def cast_car(value, cur):
    if value is None:
        return None

    m = re.match(r'\(([^)]+),([^)])\)', value)
    if m:
        return Car(m.group(1), m.group(2))
    else:
        pass


connection = psycopg2.connect(database="postgres", user="postgres", password="Wggs8m42=")

cursor = connection.cursor()

#   Inserting into a table (num, and data are the name of the columns)
one = "Toyota"
info = "Corolla"

#cursor.execute("Insert INTO test (num, data) VALUES (%s,%s);", (7, "data"))
#cursor.execute("Insert Into test (num, data) VALUES (%s,%s);", (one, info))

#Look at all the changes
#cursor.execute("Insert Into cars (car_type, car_model) VALUES (%s,%s);", (one, info))
cursor.execute('''Select * from cars''')

Toyota = Car()

Toyota = cursor.fetchone()
print(type(Toyota), Toyota)


#   commit the changes
#connection.commit()


#   and close everything
cursor.close()
connection.close()