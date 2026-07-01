class Destino:
    def __init__(self, id_destino=None, nombre="", descripcion="", actividades="", costo=0.0):
        self._id_destino = id_destino
        self._nombre = nombre
        self._descripcion = descripcion
        self._actividades = actividades
        self._costo = float(costo)

    def get_id(self): return self._id_destino
    def get_nombre(self): return self._nombre
    def get_descripcion(self): return self._descripcion
    def get_actividades(self): return self._actividades
    def get_costo(self): return self._costo

    def set_nombre(self, nombre): self._nombre = nombre
    # ... otros setters si es necesario