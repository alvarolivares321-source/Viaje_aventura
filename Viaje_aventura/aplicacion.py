import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import time

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

# ==================== IMPORTS CORREGIDOS ====================
from Dao.DAOcliente import DAOCliente
from seguridad import Seguridad  

# ==================== PALETA VERDE ====================
FONDO_PRINCIPAL = "#f0fdf4"
MENU_BG         = "#14532d"
ACCENT          = "#4ade80"
ACCENT_DARK     = "#22c55e"
TEXTO           = "#052e16"
TEXTO_CLARO     = "#86efac"
GRIS            = "#4b5563"
ROJO            = "#ef4444"

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Viajes Aventura")
        self.root.geometry("1380x780")
        self.root.minsize(1200, 680)
        self.root.configure(bg=FONDO_PRINCIPAL)

        self.intentos_fallidos = 0
        self.bloqueado_hasta = None
        self.usuario_actual = None
        self.rol_actual = None

        self.sidebar = tk.Frame(self.root, bg=MENU_BG, width=280)
        self.sidebar.place(x=0, y=0, relheight=1)
        self.sidebar.pack_propagate(False)

        self.contenido = tk.Frame(self.root, bg=FONDO_PRINCIPAL)
        self.contenido.place(x=280, y=0, relheight=1, relwidth=1, width=-280)

        self.mostrar_login()

    def _limpiar_contenido(self):
        for w in self.contenido.winfo_children():
            w.destroy()

    def _limpiar_sidebar(self):
        for w in self.sidebar.winfo_children():
            w.destroy()

    def _boton_menu(self, texto: str, comando, icono="🌿"):
        btn = tk.Button(self.sidebar, text=f"{icono}  {texto}", command=comando,
                        bg=MENU_BG, fg=TEXTO_CLARO, activebackground=ACCENT,
                        relief="flat", font=("Arial", 12, "bold"), anchor="w",
                        padx=30, height=2, cursor="hand2", bd=0)
        btn.pack(fill="x", pady=4)

    def _titulo_seccion(self, texto: str):
        tk.Label(self.contenido, text=texto, bg=FONDO_PRINCIPAL, fg=TEXTO,
                 font=("Arial", 28, "bold")).pack(anchor="w", padx=50, pady=(40, 10))
        tk.Frame(self.contenido, bg=ACCENT, height=4).pack(fill="x", padx=50, pady=(0, 25))

    # ==================== LOGIN ====================
    def mostrar_login(self):
        self._limpiar_contenido()

        frame = tk.Frame(self.contenido, bg=FONDO_PRINCIPAL)
        frame.place(relx=0.5, rely=0.45, anchor="center")

        tk.Label(frame, text="🌍 Viajes Aventura", bg=FONDO_PRINCIPAL, 
                 fg=ACCENT_DARK, font=("Arial", 42, "bold")).pack(pady=(0,5))
        tk.Label(frame, text="Tu próxima aventura comienza aquí", bg=FONDO_PRINCIPAL, 
                 fg=GRIS, font=("Arial", 14)).pack(pady=(0,40))

        tk.Label(frame, text="Usuario / RUT", bg=FONDO_PRINCIPAL, fg=TEXTO, 
                 font=("Arial", 12, "bold")).pack(anchor="w", padx=40)
        entry_user = tk.Entry(frame, width=36, font=("Arial", 11), relief="solid", bd=2)
        entry_user.pack(pady=8, ipady=10, padx=40)

        tk.Label(frame, text="Contraseña", bg=FONDO_PRINCIPAL, fg=TEXTO, 
                 font=("Arial", 12, "bold")).pack(anchor="w", padx=40)
        entry_pw = tk.Entry(frame, width=36, font=("Arial", 11), show="*", relief="solid", bd=2)
        entry_pw.pack(pady=8, ipady=10, padx=40)

        self.lbl_estado = tk.Label(frame, text="", bg=FONDO_PRINCIPAL, fg=ROJO, font=("Arial", 10))
        self.lbl_estado.pack(pady=12)

        btn_ingresar = tk.Button(frame, text="INICIAR SESIÓN", bg=ACCENT_DARK, fg="white",
                                 relief="flat", font=("Arial", 13, "bold"), width=30, height=2,
                                 cursor="hand2",
                                 command=lambda: self._procesar_login(entry_user.get().strip(), 
                                                                      entry_pw.get()))
        btn_ingresar.pack(pady=15)

        entry_user.focus_set()

    # ==================== PROCESAR LOGIN (CORREGIDO) ====================
    def _procesar_login(self, usuario, clave):
        self.lbl_estado.config(text="")

        if not usuario or not clave:
            self.lbl_estado.config(text="⚠ Ingresa usuario y contraseña", fg=ROJO)
            return

        try:
            cliente = DAOCliente().buscar(usuario)   # ← Corregido
            if cliente and Seguridad.validar_clave(clave, cliente.get_contrasena()):  # ← Corregido
                self._login_exitoso(cliente, "Cliente")
                return

            self.lbl_estado.config(text="✘ Credenciales incorrectas", fg=ROJO)
        except Exception as ex:
            self.lbl_estado.config(text=f"Error: {ex}", fg=ROJO)

    def _login_exitoso(self, usuario, rol):
        self.usuario_actual = usuario
        self.rol_actual = rol
        if rol == "Cliente":
            self._panel_cliente()
        else:
            self._panel_admin()

    # ==================== PANEL ADMIN ====================
    def _panel_admin(self):
        self._limpiar_sidebar()
        tk.Label(self.sidebar, text="🌍 Viajes Aventura", bg=MENU_BG, fg=TEXTO_CLARO, 
                 font=("Arial", 22, "bold")).pack(pady=(30, 5))
        tk.Label(self.sidebar, text="Administrador", bg=MENU_BG, fg=ACCENT, 
                 font=("Arial", 10, "bold")).pack(pady=(0,20))

        self._boton_menu("Destinos", self._vista_destinos, "🏝️")
        self._boton_menu("Paquetes", self._vista_paquetes, "🎒")
        self._boton_menu("Reservas", self._vista_reservas, "📋")
        self._boton_menu("Exportar", self._vista_exportar, "📊")
        self._boton_menu("Cerrar Sesión", self.mostrar_login, "🚪")

        self._vista_destinos()

    def _panel_cliente(self):
        self._limpiar_sidebar()
        self._boton_menu("Explorar Paquetes", self._vista_paquetes_cliente, "🌎")
        self._boton_menu("Mis Reservas", self._vista_mis_reservas, "📅")
        self._boton_menu("Cerrar Sesión", self.mostrar_login, "🚪")
        self._vista_paquetes_cliente()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()