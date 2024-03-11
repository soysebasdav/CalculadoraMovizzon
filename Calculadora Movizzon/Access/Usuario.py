class Usuario:
    """
    Clase Usuario: Representa un usuario con nombre de usuario y contraseña.

    Atributos:
    - usuario: Una cadena que representa el nombre de usuario.
    - contrasena: Una cadena que representa la contraseña del usuario.

    Métodos:
    - __init__(usuario, contrasena): Constructor de la clase Usuario.
    """
    def __init__(self, usuario, contrasena):
        """
        Constructor de la clase Usuario.

        Parámetros:
        - usuario: Una cadena que representa el nombre de usuario.
        - contrasena: Una cadena que representa la contraseña del usuario.
        """
        self.usuario = usuario
        self.contrasena = contrasena