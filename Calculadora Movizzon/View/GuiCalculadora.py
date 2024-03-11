from tkinter import *
from PIL import Image, ImageTk
import os
from Controller.CalculadoraControlador import CalculadoraControlador

class GuiCalculadora:
    
    def __init__(self):
        # Inicializar la GUI de la calculadora

        self.calcu =CalculadoraControlador(self)
        self.root = Tk()
        self.root.title("Calculadora Movizzon")
        self.root.configure(bg="#0A1433")
        self.centrarVentana()
        self.initComponents()
        
    def initComponents(self):
        # Inicializar los componentes de la interfaz gráfica

        # Ruta de la imagen
        rutaImagen = os.path.join(os.path.dirname(__file__), "..", "Imagenes", "movizzon.png")

        # Cargar la imagen utilizando PIL
        imaMoviPil = Image.open(rutaImagen)

        # Redimensionar la imagen
        imaMoviPil = imaMoviPil.resize((105, 105), Image.LANCZOS)

        # Convertir la imagen PIL a formato compatible con Tkinter
        self.img1 = ImageTk.PhotoImage(imaMoviPil)

        # Crear un widget Label para mostrar la imagen
        labImgMovizzon = Label(self.root, image=self.img1)
        labImgMovizzon.place(x=10, y=10)  # Posición de la imagen en la ventana

        labCalculadora = Label(self.root, text='Calculadora', font=("Times New Roman", 30))
        labCalculadora.configure(bg='White')
        labCalculadora.place(x=150, y=10, width=240, height=110)

        self.cajaDisplay = Entry(self.root, font=("Times New Roman", 15))
        self.cajaDisplay.place(x=10, y=130, width=380, height=50)

        # Aquí se crean los botones y se asignan los comandos correspondientes

        Button1=Button(self.root, text="1", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers("1"))
        Button1.place(x=10, y=200, width=60, height=60)
        Button2=Button(self.root, text="2", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers("2"))
        Button2.place(x=80, y=200, width=60, height=60)
        Button3=Button(self.root, text="3", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(3))
        Button3.place(x=150, y=200, width=60, height=60)
        Buttonsuma=Button(self.root, text="+", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("+"))
        Buttonsuma.place(x=260, y=200, width=60, height=60)
        Buttonresta=Button(self.root, text="-", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("-"))
        Buttonresta.place(x=330, y=200, width=60, height=60)
        Button4=Button(self.root, text="4", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(4))
        Button4.place(x=10, y=270, width=60, height=60)
        Button5=Button(self.root, text="5", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(5))
        Button5.place(x=80, y=270, width=60, height=60)
        Button6=Button(self.root, text="6", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(6))
        Button6.place(x=150, y=270, width=60, height=60)
        Buttonmultiplizacion=Button(self.root, text="*", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("*"))
        Buttonmultiplizacion.place(x=260, y=270, width=60, height=60)
        Buttondivision=Button(self.root, text="/", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("/"))
        Buttondivision.place(x=330, y=270, width=60, height=60)
        Button7=Button(self.root, text="7", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(7))
        Button7.place(x=10, y=340, width=60, height=60)
        Button8=Button(self.root, text="8", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(8))
        Button8.place(x=80, y=340, width=60, height=60)
        Button9=Button(self.root, text="9", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getNumbers(9))
        Button9.place(x=150, y=340, width=60, height=60)
        ButtonIgual=Button(self.root, text="=", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.operacion())
        ButtonIgual.place(x=260, y=340, width=60, height=60)
        ButtonLimpiar=Button(self.root, text="AC", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.clearCajaDisplay())
        ButtonLimpiar.place(x=330, y=340, width=60, height=60)
        ButtonAbrirC=Button(self.root, text="(", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("("))
        ButtonAbrirC.place(x=10, y=410, width=60, height=60)
        ButtonCerrarC=Button(self.root, text=")", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab(")"))
        ButtonCerrarC.place(x=80, y=410, width=60, height=60)
        Button0=Button(self.root, text="0", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.getLab("0"))
        Button0.place(x=150, y=410, width=60, height=60)
        ButtonBorrar=Button(self.root, text="⟵", font=("Times New Roman", 20), bg="White", command=lambda: self.calcu.borrar())
        ButtonBorrar.place(x=260, y=410, width=130, height=60)
    
    def centrarVentana(self):

        # Función para centrar la ventana en la pantalla
        anchoVentana = 400
        altoVentana = 490

        # Obtiene el ancho y alto de la pantalla
        anchoPantalla = self.root.winfo_screenwidth()
        altoPantalla = self.root.winfo_screenheight()

        # Calcula la posición para centrar la ventana
        x = (anchoPantalla // 2) - (anchoVentana // 2)
        y = (altoPantalla // 2) - (altoVentana // 2)

        # Establece la posición de la ventana
        self.root.geometry(f"{anchoVentana}x{altoVentana}+{x}+{y}")

        self.root.resizable(False,False)
    
    

