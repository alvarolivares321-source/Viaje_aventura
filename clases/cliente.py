class Cliente:
    def __init__(self, id_cliente=None, nombre="", rut="", correo="", contrasena="", telefono=""):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._rut = rut
        self._correo = correo
        self._contrasena = contrasena
        self._telefono = telefono

    def get_id(self):
        return self._id_cliente

    def get_nombre(self):
        return self._nombre

    def get_rut(self):
        return self._rut

    def get_correo(self):
        return self._correo

    def get_contrasena(self):
        return self._contrasena

    def get_telefono(self):
        return self._telefono

    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_correo(self, correo):
        self._correo = correo

    def set_telefono(self, telefono):
        self._telefono = telefono

    def set_contrasena(self, contrasena):
        self._contrasena = contrasena