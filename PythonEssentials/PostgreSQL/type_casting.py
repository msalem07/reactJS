import psycopg2

connection = psycopg2.connect(database="postgres", user="postgres", password="Wggs8m42=")

cursor = connection.cursor()

class Car:

    def __init__(self, type, model):
        self.type = type
        self.model = model

#Create Car table
##cursor.execute("CREATE TABLE cars (id serial PRIMARY KEY, car_type varchar, car_model varchar);")

#Commit Changes
#connection.commit()

def cast_car(value,cursor):
    if value is None:
        return None

