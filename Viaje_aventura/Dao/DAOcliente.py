from conexiones import Conexion
from clases.cliente import Cliente

class DAOCliente:
    def __init__(self):
        self.con = Conexion()

    def buscar(self, rut):
        self.con.conectar()
        cursor = self.con.get_cursor()
        cursor.execute("SELECT * FROM Cliente WHERE rut = %s", (rut,))
        row = cursor.fetchone()
        self.con.desconectar()
        if row:
            return Cliente(row[0], row[1], row[2], row[3], row[4], row[5])
        return None

    def registrar(self, cliente: Cliente):
        self.con.conectar()
        cursor = self.con.get_cursor()
        sql = """INSERT INTO Cliente (nombre, rut, correo, contrasena, telefono) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (cliente.get_nombre(), cliente.get_rut(), 
                             cliente.get_correo(), cliente.get_contrasena(), cliente.get_telefono()))
        self.con.conexion.commit()
        self.con.desconectar()
        return True