import customtkinter as ctk
from Telas.tela_login import TelaLogin
from Telas.tela_principal import TelaPrincipal
import os

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema Unificado de Controle Educacional - SUCE")
        self.geometry("900x600")
        self.current_prof = None
        self.login_screen = TelaLogin(self, on_login=self.on_login)
        self.login_screen.pack(fill="both", expand=True)

    def on_login(self, professor_obj):
        self.current_prof = professor_obj
        self.login_screen.pack_forget()
        self.main_screen = TelaPrincipal(self, professor_obj)
        self.main_screen.pack(fill="both", expand=True)

if __name__ == '__main__':
    app = App()
    app.mainloop()
