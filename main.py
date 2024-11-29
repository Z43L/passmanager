import flet as ft
import UI.generador as generador
import utils.sqlite as db
import utils.cifrar as cifrar
import UI.home as HomePage
import UI.passview as PassView

def main(page: ft.Page):
    app = HomePage.MyApp()
    page.add(app)

ft.app(target=main)