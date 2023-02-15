import sqlite3

latitude = ["de","ss","ww"]
longtitude = ["şş","şğ","22"]
altitude = [45,54,54]
velocity = [458,546,632]
conn = sqlite3.connect('flights.db')

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS flights(
        latitude real,
        longtidude real,
        altitude real,
        velocity real)""")

c.execute("""INSERT INTO flights VALUES(?,?,?,?)""",(latitude,longtitude,altitude,velocity))



conn.commit()

print(c.fetchall())

conn.close()
