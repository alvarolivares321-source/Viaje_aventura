
import bcrypt

class Seguridad:
    @staticmethod
    def generar_hash(password: str) -> str:
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

    @staticmethod
    def validar_clave(password_plana: str, password_encriptada: str) -> bool:
        try:
            return bcrypt.checkpw(password_plana.encode('utf-8'), password_encriptada.encode('utf-8'))
        except Exception:
            return False

    @staticmethod
    def verificar_password(password_plana: str, password_encriptada: str) -> bool:
        return Seguridad.validar_clave(password_plana, password_encriptada)

    @staticmethod
    def encriptar_clave(password: str) -> str:
        return Seguridad.generar_hash(password)