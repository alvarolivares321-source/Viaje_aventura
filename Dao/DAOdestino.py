from conexiones import Conexion
from clases.destino import Destino

class DAODestino:
    def obtener_todo(self):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return []
            cursor.execute(
                "SELECT idDestino, nombre, descripcion, actividades, costo FROM Destino"
            )
            resultados = cursor.fetchall()
            return [Destino(
                row.get("idDestino"),
                row.get("nombre", ""),
                row.get("descripcion", ""),
                row.get("actividades", ""),
                row.get("costo", 0.0)
            ) for row in resultados]

    def registrar(self, destino: Destino):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = "INSERT INTO Destino (nombre, descripcion, actividades, costo) VALUES (%s, %s, %s, %s)"
            cursor.execute(
                sql,
                (
                    destino.get_nombre(),
                    destino.get_descripcion(),
                    destino.get_actividades(),
                    destino.get_costo()
                )
            )
            con.commit()
            return True

    def actualizar(self, destino: Destino):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = "UPDATE Destino SET nombre = %s, descripcion = %s, actividades = %s, costo = %s WHERE idDestino = %s"
            cursor.execute(
                sql,
                (
                    destino.get_nombre(),
                    destino.get_descripcion(),
                    destino.get_actividades(),
                    destino.get_costo(),
                    destino.get_id()
                )
            )
            con.commit()
            return True

    def eliminar(self, destino_id):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            cursor.execute("DELETE FROM Destino WHERE idDestino = %s", (destino_id,))
            con.commit()
            return True

    # Agrega actualizar, eliminar, buscar... (siguiendo el estilo de tu eval 2)