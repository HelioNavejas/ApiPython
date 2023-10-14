from db.db import connect
from models.Helado import Helado

cursor = connect.cursor(dictionary = True)

def new(helado):
    query = "insert into helados (id, nombre, sabor) values (null, %s, %s)"
    valores = (helado.name, helado.flavor)
    cursor.execute(query, valores)
    return cursor

def view():
    query = "select * from helados"
    cursor.execute(query)
    return cursor