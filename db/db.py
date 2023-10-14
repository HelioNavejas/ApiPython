import mysql.connector
from utils.config import u, p, h, db, po

connect = mysql.connector.connect(
    user=u, password=p, host=h, database=db, port=po
)