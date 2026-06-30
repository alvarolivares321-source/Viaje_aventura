
import bcrypt

class Seguridad:
    @staticmethod
    def encriptar_clave(password: str) -> str:
        salt = bcrypt.gensalt()
        password_bytes = password.encode('utf-8')
        password_hash = bcrypt.hashpw(password_bytes, salt)
        return password_hash.decode('utf-8')

    @staticmethod
    def validar_clave(password_plana: str, password_encriptada: str) -> bool:
        try:
            return bcrypt.checkpw(password_plana.encode('utf-8'), 
                                password_encriptada.encode('utf-8'))
        except Exception:
            return False