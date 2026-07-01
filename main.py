from dao import UsuarioDAO
import seguridad

def menu_principal():
    dao_u = UsuarioDAO()
    while True:
        print("\n--- Viajes Aventura ---")
        print("1. Registrarse")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            username = input("Ingrese nombre de usuario: ")
            password = input("Ingrese contraseña: ")
            hash_pw = seguridad.generar_hash(password)
            
            dao_u.conectar()
            try:
                dao_u.registrar_usuario(username, hash_pw)
                print("¡Usuario registrado exitosamente!")
            except Exception as e:
                print(f"Error: {e}")
            finally:
                dao_u.desconectar()

        elif opcion == "2":
            username = input("Usuario: ")
            password = input("Contraseña: ")
            
            dao_u.conectar()
            usuario = dao_u.obtener_usuario_por_username(username)
            dao_u.desconectar()
            
            if usuario and seguridad.verificar_password(password, usuario['password_hash']):
                print("¡Acceso concedido! Bienvenido.")
            else:
                print("Usuario o contraseña incorrectos.")

        elif opcion == "3":
            print("¡Hasta luego!")
            break

if __name__ == "__main__":
    menu_principal()