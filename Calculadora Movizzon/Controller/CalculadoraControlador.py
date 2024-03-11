from Model.CalculadoraModelo import CalculadoraModelo
from tkinter import *
from tkinter import messagebox
class CalculadoraControlador:
    def __init__(self, guiCalculadora):
        """Inicializa el controlador de la calculadora.

        Args:
            guiCalculadora (GuiCalculadora): Instancia de la interfaz gráfica de la calculadora.
        """
        self.guiCalculadora = guiCalculadora
        self.i=0
        self.calcModelo =CalculadoraModelo()
        

    def getNumbers(self, n):
        """Método para obtener los números ingresados por el usuario.

        Args:
            n (str): Número ingresado por el usuario.
        """
        self.guiCalculadora.cajaDisplay.insert(self.i, n)
        self.i += 1
        self.i += 1

    def getLab(self, operator):
        """Método para obtener los operadores ingresados por el usuario.

        Args:
            operator (str): Operador ingresado por el usuario.
        """
        operator_length = len(operator)
        self.guiCalculadora.cajaDisplay.insert(self.i, operator)
        self.i += operator_length

    def clearCajaDisplay(self):
        """Método para limpiar la pantalla de la calculadora."""
        self.guiCalculadora.cajaDisplay.delete(0, END)

    def borrar(self):
        """Método para eliminar el último carácter de la pantalla de la calculadora."""
        display_state = self.guiCalculadora.cajaDisplay.get()
        if len(display_state):
            display_new_state = display_state[:-1]
            self.clearCajaDisplay()
            self.guiCalculadora.cajaDisplay.insert(0, display_new_state)
        else:
            self.clearCajaDisplay()
            messagebox.showerror("Clean", "Ya borro todo")

    def operacion(self):
        """Método para realizar la operación matemática ingresada por el usuario."""
        display_state = self.guiCalculadora.cajaDisplay.get()
        self.clearCajaDisplay()
        display_state = display_state.replace('x', '*')
        
        # Resolver la expresión matemática utilizando el modelo de la calculadora
        resultado = self.calcModelo.resolver_expresion(display_state)
        if resultado is not None:
            self.guiCalculadora.cajaDisplay.insert(0, resultado)
