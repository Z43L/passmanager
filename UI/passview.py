import flet as ft

class PassView(ft.UserControl):
    def __init__(self):
        super().__init__()
        self.passwords = []

    def add_password(self, password):
        self.passwords.append(password)
        self.update()

    def build(self):
        return ft.Column(
            [
                ft.ListView(
                    [ft.Text(pw) for pw in self.passwords],
                    expand=True
                ),
                ft.TextField(label="New Password", on_submit=self.on_submit),
                ft.ElevatedButton("Add Password", on_click=self.on_click)
            ]
        )

    def on_submit(self, e):
        self.add_password(e.control.value)
        e.control.value = ""
        self.update()

    def on_click(self, e):
        text_field = self.controls[1]
        self.add_password(text_field.value)
        text_field.value = ""
        self.update()

