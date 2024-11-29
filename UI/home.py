import flet as ft
import UI.generador as generador
import UI.passview as passview

class MyApp:
    def __init__(self):
        self.current_page = "home"
        self.pages = {
            "home": ft.Text("Bienvenido a la página de inicio", size=20),
            "about": generador.generar(self.navigate),
            "passview": passview.PassView().build()
        }
        self.page_container = ft.Container(expand=True)  # Contenedor para las páginas

    def navigate(self, page_name):
        self.current_page = page_name
        self.update_page()

    def update_page(self):
        self.page_container.content = self.pages[self.current_page]  # Actualiza contenido
        if self.page_container.page:  # Asegúrate de que está añadido al árbol
            self.page_container.update()

    def build(self):
        # Crear estructura principal con NavigationBar al final
        layout = ft.Column(
            [
                self.page_container,  # Contenedor para las páginas
                ft.NavigationBar(
                    destinations=[
                        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Home"),
                        ft.NavigationBarDestination(icon=ft.Icons.INFO, label="About"),
                        ft.NavigationBarDestination(icon=ft.Icons.VIEW_LIST, label="PassView"),
                    ],
                    on_change=lambda e: self.navigate(["home", "about", "passview"][e.control.selected_index]),
                ),
            ],
            expand=True,
        )

        # Inicializar contenido del contenedor
        self.page_container.content = self.pages[self.current_page]
        return layout

def main(page: ft.Page):
    app = MyApp()
    page.add(app.build())  # Añadir la estructura principal

ft.app(target=main)
