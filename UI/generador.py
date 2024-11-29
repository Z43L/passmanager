import flet as ft
import utils.cifrar as cifrar
import utils.sqlite as db
import utils.usergenerator as usergenerator
import utils.passgenerator as passgenerator

def generar(on_navigate):
    caracteres = False
    numeros = False
    mayusculas = False

    # Funciones para manejar el estado de las opciones
    def set_caracteres(e):
        nonlocal caracteres
        caracteres = e.control.value

    def set_numeros(e):
        nonlocal numeros
        numeros = e.control.value

    def set_mayusculas(e):
        nonlocal mayusculas
        mayusculas = e.control.value

    # Generar contraseña y usuario
    def generarpass():
        return passgenerator.generate_password(8, caracteres, numeros, mayusculas, True)

    def generaruser():
        return usergenerator.user_generator(8, numeros, mayusculas, True)

    # Guardar en la base de datos
    def guardar(e):
        user = generaruser()
        password = generarpass()
        cifrado_user = cifrar.cifrar_contraseña(user)
        cifrado_pass = cifrar.cifrar_contraseña(password)
        db.insert_user(cifrado_user, cifrado_pass)

    # Crear la interfaz
    return ft.Column(
        [
            ft.Row(
                [
                    ft.Checkbox(label="chars", value=caracteres, on_change=set_caracteres),
                    ft.Checkbox(label="Núms", value=numeros, on_change=set_numeros),
                    ft.Checkbox(label="uppers", value=mayusculas, on_change=set_mayusculas),
                ]
            ),
            ft.Row(
                [
                    ft.TextField(label="Contraseña Generada", value="", read_only=True, width=200, height=50),    
                ]
            ),
            ft.Row(
                [
                    ft.Button(text="Generar Contraseña", on_click=lambda e: print(generarpass())),
                ]
            ),
            ft.Row(
                [
                    ft.TextField(label="Usuario Generado", value="", read_only=True, width=200, height=50),
                ]
            ),
            ft.Row(
                [
                    ft.Button(text="Generar Usuario", on_click=lambda e: print(generaruser())),
                ]
            ),
            ft.Row(
                [
                    ft.Button(text="Guardar en BD", on_click=guardar),
                ],
                alignment=ft.MainAxisAlignment.END,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )
        
    
        
    
