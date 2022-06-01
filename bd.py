import pymysql

from dotenv import load_dotenv
load_dotenv()

from os import environ

def obtener_conexion():
    return pymysql.connect(host=environ.get('DB_HOST'),
                                port=int(environ.get('DB_PORT')),
                                user=environ.get('DB_USER'),
                                password=environ.get('DB_PASS'),
                                db=environ.get('DB_NAME'))