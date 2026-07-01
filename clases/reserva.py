from datetime import datetime

class Reserva:
    def __init__(self, id_reserva=None, cliente_id=None, paquete_id=None, 
                 fecha_reserva=None, estado="Pendiente"):
        self._id_reserva = id_reserva
        self._cliente_id = cliente_id
        self._paquete_id = paquete_id
        self._fecha_reserva = fecha_reserva or datetime.now().strftime("%Y-%m-%d")
        self._estado = estado

    def get_cliente_id(self):
        return self._cliente_id

    def get_paquete_id(self):
        return self._paquete_id

    def get_estado(self):
        return self._estado