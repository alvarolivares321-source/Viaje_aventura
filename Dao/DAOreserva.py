from conexiones import Conexion
from clases.reserva import Reserva

class DAOReserva:
    def obtener_todo(self):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return []
            cursor.execute("""
                SELECT r.idReserva, r.Cliente_idCliente, r.Paquete_idPaquete, r.estado,
                       r.fecha_reserva, c.nombre AS cliente_nombre, p.nombre AS paquete_nombre
                FROM Reserva r
                JOIN Cliente c ON r.Cliente_idCliente = c.idCliente
                JOIN PaqueteTuristico p ON r.Paquete_idPaquete = p.idPaquete
            """)
            return cursor.fetchall()

    def registrar(self, reserva: Reserva):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = """INSERT INTO Reserva (Cliente_idCliente, Paquete_idPaquete, fecha_reserva, estado) 
                     VALUES (%s, %s, %s, %s)"""
            cursor.execute(
                sql,
                (reserva.get_cliente_id(), reserva.get_paquete_id(), reserva.get_fecha_reserva(), reserva.get_estado())
            )
            con.commit()
            return True

    def actualizar(self, reserva: Reserva):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = """UPDATE Reserva SET Cliente_idCliente = %s, Paquete_idPaquete = %s, 
                     fecha_reserva = %s, estado = %s WHERE idReserva = %s"""
            cursor.execute(
                sql,
                (
                    reserva.get_cliente_id(),
                    reserva.get_paquete_id(),
                    reserva.get_fecha_reserva(),
                    reserva.get_estado(),
                    reserva.get_id()
                )
            )
            con.commit()
            return True

    def eliminar(self, reserva_id):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            cursor.execute("DELETE FROM Reserva WHERE idReserva = %s", (reserva_id,))
            con.commit()
            return True