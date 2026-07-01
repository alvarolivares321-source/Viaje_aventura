from conexiones import Conexion
from clases.Paquete_Turistico import PaqueteTuristico
from clases.destino import Destino

class DAOPaquete:
    def obtener_destinos_por_paquete(self, paquete_id):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return []
            cursor.execute(
                "SELECT d.idDestino, d.nombre, d.descripcion, d.actividades, d.costo "
                "FROM Destino d "
                "JOIN PaqueteDestino pd ON d.idDestino = pd.Destino_idDestino "
                "WHERE pd.Paquete_idPaquete = %s",
                (paquete_id,)
            )
            rows = cursor.fetchall()
            return [Destino(
                row.get("idDestino"),
                row.get("nombre", ""),
                row.get("descripcion", ""),
                row.get("actividades", ""),
                row.get("costo", 0.0)
            ) for row in rows]

    def obtener_todo(self):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return []
            cursor.execute(
                "SELECT idPaquete, nombre, descripcion, fecha_inicio, fecha_fin, precio FROM PaqueteTuristico"
            )
            rows = cursor.fetchall()
            paquetes = []
            for row in rows:
                paquete = PaqueteTuristico(
                    row.get("idPaquete"),
                    row.get("nombre", ""),
                    row.get("descripcion", ""),
                    row.get("fecha_inicio", ""),
                    row.get("fecha_fin", ""),
                    row.get("precio", 0.0)
                )
                paquete.set_destinos(self.obtener_destinos_por_paquete(paquete.get_id()))
                paquetes.append(paquete)
            return paquetes

    def obtener_por_id(self, paquete_id):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return None
            cursor.execute(
                "SELECT idPaquete, nombre, descripcion, fecha_inicio, fecha_fin, precio FROM PaqueteTuristico WHERE idPaquete = %s",
                (paquete_id,)
            )
            row = cursor.fetchone()
            if not row:
                return None
            paquete = PaqueteTuristico(
                row.get("idPaquete"),
                row.get("nombre", ""),
                row.get("descripcion", ""),
                row.get("fecha_inicio", ""),
                row.get("fecha_fin", ""),
                row.get("precio", 0.0)
            )
            paquete.set_destinos(self.obtener_destinos_por_paquete(paquete_id))
            return paquete

    def registrar(self, paquete: PaqueteTuristico):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = """INSERT INTO PaqueteTuristico 
                     (nombre, descripcion, fecha_inicio, fecha_fin, precio) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(
                sql,
                (
                    paquete.get_nombre(),
                    paquete.get_descripcion(),
                    paquete.get_fecha_inicio(),
                    paquete.get_fecha_fin(),
                    paquete.get_precio()
                )
            )
            paquete_id = cursor.lastrowid
            destinos = paquete.get_destinos() or []
            for destino in destinos:
                destino_id = destino.get_id() if hasattr(destino, 'get_id') else destino
                cursor.execute(
                    "INSERT INTO PaqueteDestino (Paquete_idPaquete, Destino_idDestino) VALUES (%s, %s)",
                    (paquete_id, destino_id)
                )
            con.commit()
            return True

    def actualizar(self, paquete: PaqueteTuristico):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = "UPDATE PaqueteTuristico SET nombre = %s, descripcion = %s, fecha_inicio = %s, fecha_fin = %s, precio = %s WHERE idPaquete = %s"
            cursor.execute(
                sql,
                (
                    paquete.get_nombre(),
                    paquete.get_descripcion(),
                    paquete.get_fecha_inicio(),
                    paquete.get_fecha_fin(),
                    paquete.get_precio(),
                    paquete.get_id()
                )
            )
            cursor.execute("DELETE FROM PaqueteDestino WHERE Paquete_idPaquete = %s", (paquete.get_id(),))
            destinos = paquete.get_destinos() or []
            for destino in destinos:
                destino_id = destino.get_id() if hasattr(destino, 'get_id') else destino
                cursor.execute(
                    "INSERT INTO PaqueteDestino (Paquete_idPaquete, Destino_idDestino) VALUES (%s, %s)",
                    (paquete.get_id(), destino_id)
                )
            con.commit()
            return True

    def eliminar(self, paquete_id):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            cursor.execute("DELETE FROM PaqueteDestino WHERE Paquete_idPaquete = %s", (paquete_id,))
            cursor.execute("DELETE FROM PaqueteTuristico WHERE idPaquete = %s", (paquete_id,))
            con.commit()
            return True
