from tkinter import messagebox
class CalculadoraModelo:
    def __init__(self):
        """Inicializa el modelo de la calculadora."""
        self.__valor1__ = 0
        self.__valor2__ = 0
        self.__resultado__ = 0

    def set_valor(self, valor):
        """Establece el primer valor de la operación."""
        self.__valor1__ = valor

    def set_valor2(self, valor):
        """Establece el segundo valor de la operación."""
        self.__valor2__ = valor

    def set_resultado(self, resultado):
        """Establece el resultado de la operación."""
        self.__resultado__ = resultado

    def sumar(self):
        """Realiza la operación de suma."""
        self.__resultado__ = self.__valor1__ + self.__valor2__

    def restar(self):
        """Realiza la operación de resta."""
        self.__resultado__ = self.__valor1__ - self.__valor2__

    def multiplicar(self):
        """Realiza la operación de multiplicación."""
        self.__resultado__ = self.__valor1__ * self.__valor2__

    def dividir(self):
        """Realiza la operación de división."""
        if self.__valor2__ == 0:
            messagebox.showerror("Error", "División por cero.")
            self.__resultado__ = None
        else:
            self.__resultado__ = self.__valor1__ / self.__valor2__

    def operar(self, op1, operador, op2):
        """Realiza la operación especificada por el operador."""
        if operador == '+':
            self.set_valor(op1)
            self.set_valor2(op2)
            self.sumar()
        elif operador == '-':
            self.set_valor(op1)
            self.set_valor2(op2)
            self.restar()
        elif operador == '*':
            self.set_valor(op1)
            self.set_valor2(op2)
            self.multiplicar()
        elif operador == '/':
            self.set_valor(op1)
            self.set_valor2(op2)
            self.dividir()
        return self.__resultado__

    def verificar_sintaxis(self, expresion):
        """Verifica la sintaxis de la expresión matemática. Si puede llegar a contener mas parentesis o cosas por el estilo"""
        count_parentesis = 0
        for caracter in expresion:
            if caracter == '(':
                count_parentesis += 1
            elif caracter == ')':
                count_parentesis -= 1
                if count_parentesis < 0:
                    return False
        return count_parentesis == 0

    def resolver_expresion(self, expresion):
        """Resuelve la expresión matemática."""
        operadores = {'+', '-', '*', '/'}
        arreglo_grande = list(expresion)

        # Pasar por el arreglo_grande y formar números con decimales
        arreglo_mediano = []
        i = 0
        while i < len(arreglo_grande):
            if arreglo_grande[i].isdigit() or '.' in str(arreglo_grande[i]):
                num = arreglo_grande[i]
                i += 1
                while i < len(arreglo_grande) and (arreglo_grande[i].isdigit() or '.' in str(arreglo_grande[i])):
                    num += arreglo_grande[i]
                    i += 1
                arreglo_mediano.append(num)
            else:
                arreglo_mediano.append(arreglo_grande[i])
                i += 1

        # Verificar sintaxis de los paréntesis
        if not self.verificar_sintaxis(arreglo_mediano):
            messagebox.showerror("Error", "Error de sintaxis: los paréntesis no están balanceados.")
            return None

        # Resolver paréntesis
        while '(' in arreglo_mediano:
            indice_inicio = arreglo_mediano.index('(')
            indice_fin = indice_inicio + 1
            par_count = 1
            for i in range(indice_inicio + 1, len(arreglo_mediano)):
                if arreglo_mediano[i] == '(':
                    par_count += 1
                elif arreglo_mediano[i] == ')':
                    par_count -= 1
                    if par_count == 0:
                        indice_fin = i
                        break
            sub_expresion = arreglo_mediano[indice_inicio + 1:indice_fin]
            resultado_peque = self.resolver_expresion(sub_expresion)
            if resultado_peque is None:
                return None
            arreglo_mediano = arreglo_mediano[:indice_inicio] + [resultado_peque] + arreglo_mediano[indice_fin + 1:]

        # Resolver expresión
        stack = []
        for token in arreglo_mediano:
            if token in operadores:
                stack.append(token)
            else:
                if '.' in str(token):
                    stack.append(float(token))
                else:
                    stack.append(token)

        while len(stack) > 1:
            op2 = stack.pop()
            operador = stack.pop()
            try:
                op1 = stack.pop()
                resultado = self.operar(float(op1), operador, float(op2))
            except Exception as e:
                messagebox.showerror("Error", "Error Syntaxis.")
                return None
            if resultado is None:
                return None
            stack.append(resultado)

        return stack[0]