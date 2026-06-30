from conexiones import Conexion
from clases.Paquete_Turistico import PaqueteTuristico

class DAOPaquete:
    def __init__(self):
        self.con = Conexion()

    def obtener_todo(self):
        self.con.conectar()
        cursor = self.con.get_cursor()
        cursor.execute("SELECT * FROM PaqueteTuristico")
        rows = cursor.fetchall()
        self.con.desconectar()
        return [PaqueteTuristico(row[0], row[1], row[2], row[3], row[4], row[5]) for row in rows]

    def registrar(self, paquete: PaqueteTuristico):
        self.con.conectar()
        cursor = self.con.get_cursor()
        sql = """INSERT INTO PaqueteTuristico 
                 (nombre, descripcion, fecha_inicio, fecha_fin, precio) 
                 VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(sql, (paquete.get_nombre(), paquete.get_descripcion(),
                             paquete.get_fecha_inicio(), paquete.get_fecha_fin(), paquete.get_precio()))
        self.con.conexion.commit()
        self.con.desconectar()
        return True