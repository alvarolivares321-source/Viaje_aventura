import mysql.connector

class UsuarioDAO:
    def __init__(self):
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': '', 
            'database': 'viajes_aventura_db'
        }
        self.conexion = None

    def conectar(self):
        self.conexion = mysql.connector.connect(**self.config)

    def desconectar(self):
        if self.conexion:
            self.conexion.close()

    def registrar_usuario(self, username, hash_pw):
        cursor = self.conexion.cursor()
        sql = "INSERT INTO usuarios (username, password_hash) VALUES (%s, %s)"
        cursor.execute(sql, (username, hash_pw))
        self.conexion.commit()
        cursor.close()

    def obtener_usuario_por_username(self, username):
        cursor = self.conexion.cursor(dictionary=True)
        sql = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(sql, (username,))
        usuario = cursor.fetchone()
        cursor.close()
        return usuario