class Cliente:
    def __init__(self, id_cliente=None, nombre="", rut="", correo="", contrasena="", telefono=""):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._rut = rut
        self._correo = correo
        self._contrasena = contrasena
        self._telefono = telefono

    def get_rut(self): return self._rut
    def get_nombre(self): return self._nombre
    def get_contrasena(self): return self._contrasena