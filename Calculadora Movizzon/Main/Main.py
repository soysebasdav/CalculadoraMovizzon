import sys
import os

# Importar módulos necesarios

# Obtener la ruta del directorio actual (donde se encuentra SegundoMain.py)
current_directory = os.path.dirname(os.path.abspath(__file__))

# Obtener la ruta del directorio padre (la raíz del proyecto)
project_root = os.path.abspath(os.path.join(current_directory, ".."))

# Agregar la ruta del proyecto al sys.path
sys.path.append(project_root)

# Importar clases y controladores

from View.GuiInicioSesion import GuiInicioSesion  # Importa la clase GuiCalculadora
from Controller.InicioSesionControlador import InicioSesionControlador

# Crear instancia de la interfaz gráfica y controlador

# Crea una instancia de GuiInicioSesion
guiInicioSesion = GuiInicioSesion()

# Pasa esa instancia al constructor de InicioSesionControlador
controlInicioSesion = InicioSesionControlador(guiInicioSesion)

# Iniciar la aplicación

# Inicia el bucle principal de Tkinter
guiInicioSesion.root.mainloop()