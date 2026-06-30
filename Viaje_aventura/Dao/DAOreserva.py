from conexiones import Conexion
from clases.reserva import Reserva

class DAOReserva:
    def __init__(self):
        self.con = Conexion()

    def obtener_todo(self):
        self.con.conectar()
        cursor = self.con.get_cursor()
        cursor.execute("""
            SELECT r.*, c.nombre as cliente_nombre, p.nombre as paquete_nombre 
            FROM Reserva r 
            JOIN Cliente c ON r.Cliente_idCliente = c.idCliente 
            JOIN PaqueteTuristico p ON r.Paquete_idPaquete = p.idPaquete
        """)
        rows = cursor.fetchall()
        self.con.desconectar()
        return rows  # Puedes mapear a objetos si prefieres

    def registrar(self, reserva: Reserva):
        self.con.conectar()
        cursor = self.con.get_cursor()
        sql = """INSERT INTO Reserva (Cliente_idCliente, Paquete_idPaquete, estado) 
                 VALUES (%s, %s, %s)"""
        cursor.execute(sql, (reserva.get_cliente_id(), reserva.get_paquete_id(), reserva.get_estado()))
        self.con.conexion.commit()
        self.con.desconectar()
        return True