from Model.InicioSesionModelo import InicioSesionModelo

class InicioSesionControlador:
    def __init__(self, guiInicioSesion):
        """Inicializa el controlador de inicio de sesión.

        Args:
            guiInicioSesion (GuiInicioSesion): Instancia de la interfaz gráfica de inicio de sesión.
        """
        self.guiInicioSesion = guiInicioSesion
        self.inise =InicioSesionModelo()

    def iniSesion(self):
        """Método para iniciar sesión."""

         # Obtener el usuario y la contraseña ingresados por el usuario desde la interfaz gráfica
        displayUsuario = self.guiInicioSesion.cajaUsuario.get()
        displayContrasena = self.guiInicioSesion.cajaContrasena.get()

        # Llamar al método de validación de inicio de sesión del modelo
        self.inise.ValidadInicio(displayUsuario,displayContrasena, self.guiInicioSesion)

        
    
    
