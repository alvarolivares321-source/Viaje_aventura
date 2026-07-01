import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '12345',
    'database': 'viajes_aventura'
}

class Conexion:
    def __init__(self, config=None):
        self._config = config or DB_CONFIG
        self._conexion = None
        self._cursor = None

    def conectar(self):
        if self._conexion and self._conexion.is_connected():
            return self._conexion
        try:
            self._conexion = mysql.connector.connect(**self._config)
            self._cursor = self._conexion.cursor(dictionary=True)
            return self._conexion
        except Error as e:
            print(f"❌ Error de conexión: {e}")
            self._conexion = None
            self._cursor = None
            return None

    def desconectar(self):
        if self._cursor:
            try:
                self._cursor.close()
            except Exception:
                pass
            self._cursor = None

        if self._conexion and self._conexion.is_connected():
            try:
                self._conexion.close()
            except Exception:
                pass
            self._conexion = None

    def get_cursor(self):
        return self._cursor

    def commit(self):
        if self._conexion and self._conexion.is_connected():
            self._conexion.commit()

    def __enter__(self):
        self.conectar()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type and self._conexion and self._conexion.is_connected():
            try:
                self._conexion.rollback()
            except Exception:
                pass
        self.desconectar()