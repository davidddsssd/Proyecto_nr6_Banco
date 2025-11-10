import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from iu.iu_consultas import datos_consulta_saldo, datos_consulta_movimientos
from iu.iu_transacciones import datos_deposito, datos_retiro, datos_transferencia
from negocio.negocio_transacciones import realizar_deposito, realizar_retiro, realizar_transferencia
from negocio.negocio_consultas import consultar_saldo, listar_movimientos
from negocio.negocio_cliente import crear_cliente
from negocio.negocio_cuentas import crear_cuenta

# --- Definición de Colores (Inspirado en el HTML) ---
DARK_BG = '#111827'        # bg-gray-900 (Fondo de la ventana)
FRAME_BG = '#1F2937'       # bg-gray-800 (Fondo del "card")
BUTTON_BG = '#374151'      # bg-gray-700 (Botón normal)
BUTTON_HOVER = '#4B5563'   # bg-gray-600 (Botón hover/back)
CYAN = '#22D3EE'           # text-cyan-400 (Títulos)
CYAN_HOVER = '#06B6D4'     # bg-cyan-600 (Botón primario)
WHITE = '#F9FAFB'          # text-gray-100
GRAY_TEXT = '#9CA3AF'      # text-gray-400
ENTRY_BG = '#374151'       # bg-gray-700 (Inputs)
ENTRY_BORDER = '#4B5563'   # border-gray-600
FONT_FAMILY = 'Inter'

class BancoApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("Sistema de Gestión Bancaria")
        self.geometry("450x550")
        self.configure(bg=DARK_BG)

        # Configurar estilos
        self.setup_styles()

        # Contenedor principal
        container = ttk.Frame(self, style='Main.TFrame')
        container.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        # Lista de todas las vistas
        for F in (MainMenu, AdminMenu, ClientMenu, RegisterClientView, CreateAccountView,
                 ConsultarSaldoView, VerMovimientosView, DepositarView, RetirarView, TransferirView):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(MainMenu)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def setup_styles(self):
        style = ttk.Style(self)
        style.theme_use('clam')
        
        # Configuración base
        style.configure('.',
            background=FRAME_BG,
            foreground=WHITE,
            font=(FONT_FAMILY, 11))

        # Frame principal
        style.configure('Main.TFrame',
            background=FRAME_BG)

        # Títulos
        style.configure('Header.TLabel',
            foreground=CYAN,
            background=FRAME_BG,
            font=(FONT_FAMILY, 16, 'bold'))

        # Etiquetas
        style.configure('TLabel',
            background=FRAME_BG,
            foreground=WHITE,
            font=(FONT_FAMILY, 11))

        # Botones navegación
        style.configure('TButton',
            background=BUTTON_BG,
            foreground=WHITE,
            font=(FONT_FAMILY, 11, 'bold'),
            padding=(10, 12))
        
        style.map('TButton',
            background=[('active', CYAN_HOVER)],
            foreground=[('active', WHITE)])

        # Botón volver
        style.configure('Back.TButton',
            background=BUTTON_HOVER)
        
        # Botón acción
        style.configure('Action.TButton',
            background=CYAN_HOVER)

        # Entradas
        style.configure('TEntry',
            fieldbackground=ENTRY_BG,
            foreground=WHITE)

        # Combobox
        style.configure('TCombobox',
            fieldbackground=ENTRY_BG,
            foreground=WHITE)

class MainMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="*** Bienvenido al Sistema de Gestión Bancaria ***", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Button(self, text="[1] Ingresar como Cliente",
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=1, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="[2] Ingresar como Administrador",
                  command=lambda: controller.show_frame(AdminMenu)).grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="[0] Salir",
                  style='Back.TButton',
                  command=controller.quit).grid(row=3, column=0, pady=5, padx=20, sticky='ew')

class AdminMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="*** Menú del Administrador ***", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Button(self, text="[1] Registrar nuevo cliente",
                  command=lambda: controller.show_frame(RegisterClientView)).grid(row=1, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="[2] Crear cuenta bancaria",
                  command=lambda: controller.show_frame(CreateAccountView)).grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="[0] Volver al menú anterior",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(MainMenu)).grid(row=3, column=0, pady=5, padx=20, sticky='ew')

class RegisterClientView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_columnconfigure(1, weight=1)

        ttk.Label(self, text="Registrar Nuevo Cliente", 
                 style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=20)

        # Campos del formulario
        campos = [("Nombre:", "nombre"), ("Apellido:", "apellido"), 
                 ("RUT:", "rut"), ("Teléfono:", "telefono"), 
                 ("Correo (opcional):", "mail")]

        self.entries = {}
        for i, (label, campo) in enumerate(campos, 1):
            ttk.Label(self, text=label).grid(row=i, column=0, padx=(20,10), pady=5, sticky='w')
            self.entries[campo] = ttk.Entry(self)
            self.entries[campo].grid(row=i, column=1, padx=(0,20), pady=5, sticky='ew')

        # Botones
        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(AdminMenu)).grid(row=len(campos)+1, column=0, pady=20, padx=20, sticky='ew')

        ttk.Button(self, text="Registrar",
                  style='Action.TButton',
                  command=self.registrar_cliente).grid(row=len(campos)+1, column=1, pady=20, padx=20, sticky='ew')

    def registrar_cliente(self):
        datos = {campo: entry.get().strip() for campo, entry in self.entries.items()}
        
        # Validaciones básicas
        if not datos['nombre'] or not datos['rut']:
            messagebox.showerror("Error", "Nombre y RUT son obligatorios")
            return

        try:
            # Llamar a la función de negocio
            crear_cliente(datos['nombre'], datos['apellido'], datos['rut'], 
                        datos['telefono'], datos['mail'])
            messagebox.showinfo("Éxito", "Cliente registrado correctamente")
            self.controller.show_frame(AdminMenu)
        except Exception as e:
            messagebox.showerror("Error", str(e))

class CreateAccountView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_columnconfigure(1, weight=1)

        ttk.Label(self, text="Crear Cuenta Bancaria", 
                 style='Header.TLabel').grid(row=0, column=0, columnspan=2, pady=20)

        # Campos del formulario
        ttk.Label(self, text="ID del Cliente:").grid(row=1, column=0, padx=(20,10), pady=5, sticky='w')
        self.id_cliente = ttk.Entry(self)
        self.id_cliente.grid(row=1, column=1, padx=(0,20), pady=5, sticky='ew')

        ttk.Label(self, text="Número de Cuenta:").grid(row=2, column=0, padx=(20,10), pady=5, sticky='w')
        self.numero_cuenta = ttk.Entry(self)
        self.numero_cuenta.grid(row=2, column=1, padx=(0,20), pady=5, sticky='ew')

        ttk.Label(self, text="Tipo de Cuenta:").grid(row=3, column=0, padx=(20,10), pady=5, sticky='w')
        self.tipo_cuenta = ttk.Combobox(self, values=["corriente", "ahorro", "vista"])
        self.tipo_cuenta.grid(row=3, column=1, padx=(0,20), pady=5, sticky='ew')

        ttk.Label(self, text="Saldo Inicial:").grid(row=4, column=0, padx=(20,10), pady=5, sticky='w')
        self.saldo = ttk.Entry(self)
        self.saldo.grid(row=4, column=1, padx=(0,20), pady=5, sticky='ew')

        # Botones
        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(AdminMenu)).grid(row=5, column=0, pady=20, padx=20, sticky='ew')

        ttk.Button(self, text="Crear Cuenta",
                  style='Action.TButton',
                  command=self.crear_cuenta).grid(row=5, column=1, pady=20, padx=20, sticky='ew')

    def crear_cuenta(self):
        try:
            id_cliente = self.id_cliente.get().strip()
            numero_c = self.numero_cuenta.get().strip()
            tipo = self.tipo_cuenta.get()
            saldo = float(self.saldo.get().strip())

            crear_cuenta(id_cliente, numero_c, saldo, tipo)
            messagebox.showinfo("Éxito", "Cuenta creada correctamente")
            self.controller.show_frame(AdminMenu)
        except ValueError:
            messagebox.showerror("Error", "El saldo debe ser un número válido")
        except Exception as e:
            messagebox.showerror("Error", str(e))

class ClientMenu(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="*** Menú del Cliente ***", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        opciones = [
            ("Consultar saldo", ConsultarSaldoView),
            ("Ver movimientos", VerMovimientosView),
            ("Depositar dinero", DepositarView),
            ("Retirar dinero", RetirarView),
            ("Transferir dinero", TransferirView)
        ]

        for i, (texto, vista) in enumerate(opciones, 1):
            ttk.Button(self, text=f"[{i}] {texto}",
                      command=lambda v=vista: controller.show_frame(v)).grid(row=i, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="[0] Volver al menú anterior",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(MainMenu)).grid(row=len(opciones)+1, column=0, pady=5, padx=20, sticky='ew')

class ConsultarSaldoView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Consultar Saldo", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Label(self, text="Número de cuenta:").grid(row=1, column=0, pady=5)
        self.cuenta = ttk.Entry(self)
        self.cuenta.grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Consultar",
                  command=self.consultar).grid(row=3, column=0, pady=5, padx=20, sticky='ew')

        self.resultado = ttk.Label(self, text="")
        self.resultado.grid(row=4, column=0, pady=20)

        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=5, column=0, pady=5, padx=20, sticky='ew')

    def consultar(self):
        try:
            cuenta = self.cuenta.get().strip()
            if cuenta:
                resultado = consultar_saldo(cuenta)
                self.resultado.configure(text=f"Saldo: ${resultado:,.2f}")
            else:
                messagebox.showwarning("Error", "Ingrese un número de cuenta")
        except Exception as e:
            messagebox.showerror("Error", str(e))

# Vistas similares para otras operaciones...
class VerMovimientosView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Ver Movimientos", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Label(self, text="Número de cuenta:").grid(row=1, column=0, pady=5)
        self.cuenta = ttk.Entry(self)
        self.cuenta.grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Consultar",
                  command=self.ver_movimientos).grid(row=3, column=0, pady=5, padx=20, sticky='ew')

        self.resultado = ttk.Label(self, text="")
        self.resultado.grid(row=4, column=0, pady=20)

        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=5, column=0, pady=5, padx=20, sticky='ew')

    def ver_movimientos(self):
        try:
            cuenta = self.cuenta.get().strip()
            if cuenta:
                movimientos = listar_movimientos(cuenta)
                # Aquí podrías mostrar los movimientos en una tabla o lista
                self.resultado.configure(text=str(movimientos))
            else:
                messagebox.showwarning("Error", "Ingrese un número de cuenta")
        except Exception as e:
            messagebox.showerror("Error", str(e))

class DepositarView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Depositar Dinero", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Label(self, text="Número de cuenta:").grid(row=1, column=0, pady=5)
        self.cuenta = ttk.Entry(self)
        self.cuenta.grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Label(self, text="Monto:").grid(row=3, column=0, pady=5)
        self.monto = ttk.Entry(self)
        self.monto.grid(row=4, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Depositar",
                  style='Action.TButton',
                  command=self.depositar).grid(row=5, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=6, column=0, pady=5, padx=20, sticky='ew')

    def depositar(self):
        try:
            cuenta = self.cuenta.get().strip()
            monto = float(self.monto.get().strip())
            realizar_deposito(cuenta, monto)
            messagebox.showinfo("Éxito", "Depósito realizado correctamente")
            self.controller.show_frame(ClientMenu)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")
        except Exception as e:
            messagebox.showerror("Error", str(e))

class RetirarView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Retirar Dinero", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Label(self, text="Número de cuenta:").grid(row=1, column=0, pady=5)
        self.cuenta = ttk.Entry(self)
        self.cuenta.grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Label(self, text="Monto:").grid(row=3, column=0, pady=5)
        self.monto = ttk.Entry(self)
        self.monto.grid(row=4, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Retirar",
                  style='Action.TButton',
                  command=self.retirar).grid(row=5, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=6, column=0, pady=5, padx=20, sticky='ew')

    def retirar(self):
        try:
            cuenta = self.cuenta.get().strip()
            monto = float(self.monto.get().strip())
            realizar_retiro(cuenta, monto)
            messagebox.showinfo("Éxito", "Retiro realizado correctamente")
            self.controller.show_frame(ClientMenu)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")
        except Exception as e:
            messagebox.showerror("Error", str(e))

class TransferirView(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, style='Main.TFrame')
        self.controller = controller
        self.grid_columnconfigure(0, weight=1)

        ttk.Label(self, text="Transferir Dinero", 
                 style='Header.TLabel').grid(row=0, column=0, pady=20)

        ttk.Label(self, text="Cuenta origen:").grid(row=1, column=0, pady=5)
        self.cuenta_origen = ttk.Entry(self)
        self.cuenta_origen.grid(row=2, column=0, pady=5, padx=20, sticky='ew')

        ttk.Label(self, text="Cuenta destino:").grid(row=3, column=0, pady=5)
        self.cuenta_destino = ttk.Entry(self)
        self.cuenta_destino.grid(row=4, column=0, pady=5, padx=20, sticky='ew')

        ttk.Label(self, text="Monto:").grid(row=5, column=0, pady=5)
        self.monto = ttk.Entry(self)
        self.monto.grid(row=6, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Transferir",
                  style='Action.TButton',
                  command=self.transferir).grid(row=7, column=0, pady=5, padx=20, sticky='ew')

        ttk.Button(self, text="Volver",
                  style='Back.TButton',
                  command=lambda: controller.show_frame(ClientMenu)).grid(row=8, column=0, pady=5, padx=20, sticky='ew')

    def transferir(self):
        try:
            origen = self.cuenta_origen.get().strip()
            destino = self.cuenta_destino.get().strip()
            monto = float(self.monto.get().strip())
            realizar_transferencia(origen, destino, monto)
            messagebox.showinfo("Éxito", "Transferencia realizada correctamente")
            self.controller.show_frame(ClientMenu)
        except ValueError:
            messagebox.showerror("Error", "El monto debe ser un número válido")
        except Exception as e:
            messagebox.showerror("Error", str(e))

def iniciar_interfaz():
    app = BancoApp()
    app.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
