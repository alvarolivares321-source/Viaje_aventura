class Reserva:
    def __init__(self, id_reserva=None, cliente=None, paquete=None, fecha_reserva=None, estado="Pendiente"):
        self._id_reserva = id_reserva
        self._cliente = cliente
        self._paquete = paquete
        self._fecha_reserva = fecha_reserva or datetime.now().strftime("%Y-%m-%d")
        self._estado = estado