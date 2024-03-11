import sys
import os

# Obtener la ruta del directorio actual (donde se encuentra SegundoMain.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta del directorio padre (la raíz del proyecto)
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Agregar la ruta del proyecto al sys.path
sys.path.append(project_root)

from Access.Usuario import Usuario
from Access.UsuarioDAO import UsuarioDAO
from Access.APIDAO import APIDAO
# Importa la clase GuiCalculadora
from View.GuiCalculadora import GuiCalculadora
from Controller.CalculadoraControlador import CalculadoraControlador
import time

class InicioSesionModelo:
    def __init__(self):
        """Inicializa el modelo de inicio de sesión."""
        self.__Usuario__ = ""
        self.__Contrasena__ = ""
        self.__resultado__ = 0

    def setUsuario(self, Usuario):
        """Establece el nombre de usuario."""
        self.__Usuario__ = Usuario
    
    def setContrasena(self, Contrasena):
        """Establece la contraseña."""
        self.__Contrasena__ = Contrasena
        
    def ValidadInicio(self, User, Pass, guiIni):
        """Valida las credenciales de inicio de sesión del usuario.

        Args:
            User (str): Nombre de usuario.
            Pass (str): Contraseña.
            guiIni (GuiInicioSesion): Instancia de la interfaz gráfica de inicio de sesión.
        """
        # Establecer el usuario y la contraseña
        self.setUsuario(User)
        self.setContrasena(Pass)

        # Crear un objeto Usuario
        usuarioObj = Usuario(self.__Usuario__, self.__Contrasena__)

        # Crear una instancia de APIDAO
        dao = APIDAO()

        # Autenticar el usuario utilizando el objeto APIDAO
        if dao.autenticar(usuarioObj):
            # Autenticación exitosa
            
            # Destruir la ventana de inicio de sesión
            guiInicioSesion = guiIni
            guiInicioSesion.root.destroy()

            # Crea una instancia de GuiCalculadora
            guiCalculadora = GuiCalculadora()

             # Crear una instancia de CalculadoraControlador y pasar la instancia de GuiCalculadora
            controlCalculadora = CalculadoraControlador(guiCalculadora)

            # Iniciar el bucle principal de Tkinter para mostrar la calculadora
            guiCalculadora.root.mainloop()
        else:
            print("Error de autenticación.")