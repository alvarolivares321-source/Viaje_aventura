from conexiones import Conexion
from clases.cliente import Cliente

class DAOCliente:
    def buscar(self, rut):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return None
            cursor.execute(
                "SELECT idCliente, nombre, rut, correo, contrasena, telefono "
                "FROM Cliente WHERE rut = %s",
                (rut,)
            )
            row = cursor.fetchone()
            if row:
                return Cliente(
                    row.get("idCliente"),
                    row.get("nombre", ""),
                    row.get("rut", ""),
                    row.get("correo", ""),
                    row.get("contrasena", ""),
                    row.get("telefono", "")
                )
        return None

    def obtener_todo(self):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return []
            cursor.execute(
                "SELECT idCliente, nombre, rut, correo, telefono FROM Cliente"
            )
            rows = cursor.fetchall()
            return [Cliente(
                row.get("idCliente"),
                row.get("nombre", ""),
                row.get("rut", ""),
                row.get("correo", ""),
                "",
                row.get("telefono", "")
            ) for row in rows]

    def registrar(self, cliente: Cliente):
        with Conexion() as con:
            cursor = con.get_cursor()
            if not cursor:
                return False
            sql = """INSERT INTO Cliente (nombre, rut, correo, contrasena, telefono) 
                     VALUES (%s, %s, %s, %s, %s)"""
            cursor.execute(
                sql,
                (
                    cliente.get_nombre(),
                    cliente.get_rut(),
                    cliente.get_correo(),
                    cliente.get_contrasena(),
                    cliente.get_telefono()
                )
            )
            con.commit()
            return True