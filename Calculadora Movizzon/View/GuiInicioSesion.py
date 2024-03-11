from tkinter import *
from PIL import Image, ImageTk
import os
from Controller.InicioSesionControlador import InicioSesionControlador

class GuiInicioSesion:

    def __init__(self):

        # Inicialización de la interfaz de inicio de sesión

        # Crear instancia del controlador de inicio de sesión
        self.inise =InicioSesionControlador(self)

        # Crear ventana principal
        self.root = Tk()
        self.root.title("Inicio Sesion Movizzon API")
        self.root.configure(bg="#0A1433")
        self.centrarVentana()
        self.initComponents()

    def initComponents(self):
        # Inicialización de componentes de la interfaz

        # Ruta de la imagen del logo
        rutaImagen = os.path.join(os.path.dirname(__file__), "..", "Imagenes", "movizzon.png")

        # Cargar y redimensionar la imagen del logo
        imaMoviPil = Image.open(rutaImagen)
        imaMoviPil = imaMoviPil.resize((150, 150), Image.LANCZOS)

        # Convertir imagen PIL a formato compatible con Tkinter
        self.img1 = ImageTk.PhotoImage(imaMoviPil)

        # Crear widget Label para mostrar el logo
        labImgMovizzon = Label(self.root, image=self.img1)
        labImgMovizzon.place(x=125, y=50)  # Posición de la imagen en la ventana 70

        # Crear etiquetas y cajas de entrada para usuario y contraseña
        labUsuario = Label(self.root, text='Usuario', font=("Times New Roman", 15), fg='white')
        labUsuario.configure(bg='#0A1433')
        labUsuario.place(x=50, y=230)

        labContrasena = Label(self.root, text='Contraseña', font=("Times New Roman", 15), fg='white')
        labContrasena.configure(bg='#0A1433')
        labContrasena.place(x=50, y=310)

        self.cajaUsuario = Entry(self.root, font=("Times New Roman", 15))
        self.cajaUsuario.place(x=50, y=260, width=300, height=30)

        self.cajaContrasena = Entry(self.root, font=("Times New Roman", 15))
        self.cajaContrasena.place(x=50, y=340, width=300, height=30)

        # Botón de inicio de sesión
        ButtonInicioSesion=Button(self.root, text="Inicie Sesión", font=("Times New Roman", 15), bg="White", command=lambda: self.inise.iniSesion())
        ButtonInicioSesion.place(x=130, y=410, width=140, height=40)

    def centrarVentana(self):
        # Centrar la ventana en la pantalla

        # Tamaño de la ventana
        anchoVentana = 400
        altoVentana = 490

        # Tamaño de la pantalla
        anchoPantalla = self.root.winfo_screenwidth()
        altoPantalla = self.root.winfo_screenheight()

        # Establecer la posición de la ventana
        x = (anchoPantalla // 2) - (anchoVentana // 2)
        y = (altoPantalla // 2) - (altoVentana // 2)

        # Bloquear el redimensionamiento de la ventana
        self.root.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")

        self.root.resizable(False,False)

