# conexiones.py
import mysql.connector
from mysql.connector import Error

class Conexion:
    def __init__(self):
        self.__conexion = None
        self.__cursor = None

    def conectar(self):
        try:
            self.__conexion = mysql.connector.connect(
                host='localhost',
                user='root',           # cambia si tienes otro usuario
                password='12345',           # pon tu contraseña
                database='viajes_aventura'
            )
            self.__cursor = self.__conexion.cursor()
            return self.__conexion
        except Error as e:
            print(f"Error de conexión: {e}")
            return None

    def desconectar(self):
        if self.__conexion:
            self.__conexion.close()

    def get_cursor(self):
        return self.__cursor