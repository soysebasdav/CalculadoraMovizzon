import requests
import time
from Access.Usuario import Usuario
from Access.UsuarioDAO import UsuarioDAO
from tkinter import messagebox

class APIDAO(UsuarioDAO):
    """
    Clase APIDAO: Maneja las solicitudes a una API "Movizzon" para autenticar usuarios.

    Atributos:
    - No tiene atributos adicionales.

    Métodos:
    - autenticar(usuario): Autentica un usuario mediante una solicitud a una API.
    """
    def autenticar(self, usuario):
        """
        Autentica un usuario utilizando una solicitud a una API Movizzon "Prueba de Desarrollo".

        Parámetros:
        - usuario: Un objeto de la clase Usuario que contiene el nombre de usuario y la contraseña.

        Devoluciones:
        - True si la autenticación es exitosa, False de lo contrario.
        """

        # URL de la API de autenticación
        url = 'https://7llhy2yytb.execute-api.us-east-2.amazonaws.com/default/PruebaDesarrollo'

        # Datos a enviar en la solicitud POST
        datos = {
            "user": usuario.usuario,
            "password": usuario.contrasena
        }
        
        try:
            response = requests.post(url, json=datos)
            
            if response.status_code == 200 :
                messagebox.showinfo("Estado", f"¡Código de acceso exitoso! El código es {response.status_code}")
                
                return True
            elif response.status_code == 403:
                messagebox.showerror("Estado", f"¡Código de acceso fallido! El código es {response.status_code}")
                
                return False
            elif response.status_code == 500:
                messagebox.showerror("Estado", f"¡Error con la coxión de la API! El código es {response.status_code}")
                
                return False
            else:
                messagebox.showerror("Estado", f"Error desconocido. Código de estado: {response.status_code}")
                
                return False
        except requests.exceptions.RequestException as e:
            # Capturar excepciones de solicitud y mostrar un mensaje de advertencia
            messagebox.showwarning("ERROR", f"ERROR. Código de estado: {response.status_code}")
            time.sleep(1)  # Pausa de 1 segundo antes de reintentar
            return False