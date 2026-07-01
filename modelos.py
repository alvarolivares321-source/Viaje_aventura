class Usuario:
     def __init__(self, username, password_hash, id_usuario=None):
        self.id_usuario = id_usuario
        self.username = username
        self.password_hash = password_hash


class Destino:
    def __init__(self, nombre, descripcion, actividades, costo, id_destino=None):
        self.id_destino = id_destino
        self.nombre = nombre
        self.descripcion = descripcion
        self.actividades = actividades
        self.costo = costo


class PaqueteTuristico:
    def __init__(self, nombre, destinos, fecha_inicio, fecha_fin, id_paquete=None):
        self.id_paquete = id_paquete
        self.nombre = nombre
        self.destinos = destinos  # Esto será una lista de objetos de tipo Destino
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.precio_total = self.calcular_precio()

    def calcular_precio(self):
        total = 0
        for destino in self.destinos:
            total += float(destino.costo)
        return total


class Reserva:
    def __init__(self, id_usuario, id_paquete, fecha_reserva, id_reserva=None):
        self.id_reserva = id_reserva
        self.id_usuario = id_usuario
        self.id_paquete = id_paquete
        self.fecha_reserva = fecha_reserva