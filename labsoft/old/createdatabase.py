import sqlite3
import datetime
import time
from administradorvehiculos.db import BaseDeDato



db = BaseDeDato.BaseDeDatos()
#creamos una conexion
#si no existe la crea
#conn = sqlite3.connect('turorial.db')


#definir el cursor
#como para poder navegar no lo entiendo muy bien
#c = conn.cursor()

def create_table():


    db.c.execute('CREATE TABLE IF NOT EXISTS estudiante(id INT, name TEXT, date TEXT )')




def insertEstudiantes():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d'))
    print(date)
    db.c.execute('INSERT INTO estudiante (name, date) VALUES (?,?)',('felipe', date))

    db.conn.commit()

print(create_table())
for i in range(10):

    insertEstudiantes()

db.Cerrar()
