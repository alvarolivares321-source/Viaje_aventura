from conexiones import Conexion
from clases.destino import Destino

class DAODestino:
    def __init__(self):
        self.conexion = Conexion()

    def obtener_todo(self):
        self.conexion.conectar()
        cursor = self.conexion.get_cursor()
        cursor.execute("SELECT * FROM Destino")
        resultados = cursor.fetchall()
        destinos = []
        for row in resultados:
            destinos.append(Destino(row[0], row[1], row[2], row[3], row[4]))
        self.conexion.desconectar()
        return destinos

    def registrar(self, destino: Destino):
        self.conexion.conectar()
        cursor = self.conexion.get_cursor()
        sql = "INSERT INTO Destino (nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (destino.get_nombre(), destino.get_descripcion(), 
                           destino.get_actividades(), destino.get_costo()))
        self.conexion.conexion.commit()
        self.conexion.desconectar()

    # Agrega actualizar, eliminar, buscar... (siguiendo el estilo de tu eval 2)