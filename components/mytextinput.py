import flet as ft

"""
    este es un componente personalizado que hereda de ft.TextInput
    con un constructor que recibe un texto y lo pasa al constructor de la clase padre
    este componente es un input con un fondo blanco y texto negro con pequeños bordes
    redondeados 
    tiene una funcion que valida  que el placeholder no este vacio
"""

class MyTextInput:
    def __init__(self, text="escribe..."):
        super().__init__(text)
        self.placeholder = text
        self.bgcolor = ft.Colors.WHITE
        self.textcolor = ft.Colors.BLACK
        self.width = 50
        self.height = 50
        self.shape = ft.RoundedRectangleBorder(radius=10)
                
    def validate(self):
        if self.text == "":
            self.error = "no puedes dejar este campo vacio"
            self.update()
            return False
        self.error = None
        self.update()
        return True
            
        