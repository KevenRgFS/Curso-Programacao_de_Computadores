import customtkinter as ctk
from tkinter import messagebox
from Telas.tela_alunos import TelaAlunos

class TelaPrincipal(ctk.CTkFrame):
    def __init__(self, master, professor):
        super().__init__(master)
        self.professor = professor
        self.configure(fg_color="#153b2f")
        self._build()

    def _build(self):
        top = ctk.CTkFrame(self, fg_color="#1b3b30")
        top.pack(fill="x", padx=8, pady=8)
        ctk.CTkLabel(top, text=f"Olá, {self.professor.nome}", font=("", 16, "bold"), text_color="#9cf4ae").pack(side="left", padx=10)
        ctk.CTkButton(top, text="Sair", width=80, command=self._sair).pack(side="right", padx=10)

        body = ctk.CTkFrame(self, fg_color="#153b2f")
        body.pack(fill="both", expand=True, padx=8, pady=8)

#barrinha Lateral
        menu = ctk.CTkFrame(body, width=220, fg_color="#1f6650")
        menu.pack(side="left", fill="y", padx=(0,8), pady=6)
        ctk.CTkLabel(menu, text="Menu", text_color="#9cf4ae").pack(pady=6)
        ctk.CTkButton(menu, text="Alunos", width=180, command=lambda: self.Mostrar_area('alunos')).pack(pady=6)
        ctk.CTkButton(menu, text="Avaliações", width=180, command=lambda: self.Mostrar_area('avaliacoes')).pack(pady=6)
        ctk.CTkButton(menu, text="Turmas", width=180, command=lambda: self.Mostrar_area('turmas')).pack(pady=6)

        self.content = ctk.CTkFrame(body, fg_color="#153b2f")
        self.content.pack(side="left", fill="both", expand=True, pady=6)

        self.Mostrar_area('alunos')

    def Mostrar_area(self, area):
        for w in self.content.winfo_children():
            w.destroy()
        if area == 'alunos':
            TelaAlunos(self.content).pack(fill="both", expand=True)
        elif area == 'turmas':
            ctk.CTkLabel(self.content, text="...", text_color="#9cf4ae").pack(padx=10, pady=10)
        else:
            ctk.CTkLabel(self.content, text="Área de avaliações (em breve)", text_color="#9cf4ae").pack(padx=10, pady=10)

    def _sair(self):
        self.master.destroy()
