import flet as ft


"""
    este es un componente personalizado que hereda de ft.ElebatedButton
    con un constructor que recibe un texto y lo pasa al constructor de la clase padre
    este componente es un boton con un fondo azul y texto blanco
    y un radio de 25 para que sea redondeado
"""

class MyButton(ft.ElebatedButton):
    def __init__(self, text):
        super().__init__(text)
        self.bgcolor = ft.Colors.BLUE
        self.textcolor = ft.Colors.WHITE
        self.width = 50
        self.height = 50
        self.shape = ft.RoundedRectangleBorder(radius=25)
