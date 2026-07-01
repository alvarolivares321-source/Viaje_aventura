class PaqueteTuristico:
    def __init__(self, id_paquete=None, nombre="", descripcion="", fecha_inicio="", fecha_fin="", precio=0.0, destinos=None):
        self._id_paquete = id_paquete
        self._nombre = nombre
        self._descripcion = descripcion
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = fecha_fin
        self._precio = float(precio)
        self._destinos = destinos or []

    def get_id(self): return self._id_paquete
    def get_nombre(self): return self._nombre
    def get_descripcion(self): return self._descripcion
    def get_fecha_inicio(self): return self._fecha_inicio
    def get_fecha_fin(self): return self._fecha_fin
    def get_precio(self): return self._precio
    def get_destinos(self): return self._destinos

    def set_nombre(self, nombre): self._nombre = nombre
    def set_descripcion(self, descripcion): self._descripcion = descripcion
    def set_fecha_inicio(self, fecha_inicio): self._fecha_inicio = fecha_inicio
    def set_fecha_fin(self, fecha_fin): self._fecha_fin = fecha_fin
    def set_precio(self, precio): self._precio = float(precio)
    def set_destinos(self, destinos): self._destinos = destinos