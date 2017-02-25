import psycopg2

try:
    connection = psycopg2.connect(database="postgre", user="postgre", password="Wggs8m42")
except psycopg2.Warning as w:
    print(w)
except psycopg2.Error as e:
    print(e)


