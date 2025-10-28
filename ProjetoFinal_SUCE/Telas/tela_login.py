import customtkinter as ctk
from tkinter import messagebox
import json, os
from professor import Professor

BASE = os.path.join(os.path.dirname(__file__), "..", "Dados")
PROF_FILE = os.path.join(BASE, "professores.json")

def InfoDos_professores():
    if not os.path.exists(PROF_FILE):
        return {}
    with open(PROF_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_professores(d):
    with open(PROF_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)

class TelaLogin(ctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.on_login = on_login
        self.configure(fg_color="#153b2f")
        self._build()

    def _build(self):
        titulo = ctk.CTkLabel(self, text="SUCE - Login", font=("", 22, "bold"), text_color="#9cf4ae")
        titulo.pack(pady=(24,8))

        frm = ctk.CTkFrame(self, fg_color="#1f6650")
        frm.pack(padx=18, pady=12)

        ctk.CTkLabel(frm, text="Email:", text_color="#9cf4ae").grid(row=0, column=0, padx=6, pady=6, sticky="w")
        self.email = ctk.CTkEntry(frm, width=300, fg_color="#3d7961")
        self.email.grid(row=0, column=1, padx=6, pady=6)

        ctk.CTkLabel(frm, text="Senha:", text_color="#9cf4ae").grid(row=1, column=0, padx=6, pady=6, sticky="w")
        self.senha = ctk.CTkEntry(frm, width=300, show="*", fg_color="#3d7961")
        self.senha.grid(row=1, column=1, padx=6, pady=6)

        btns = ctk.CTkFrame(self, fg_color="#153b2f")
        btns.pack(pady=12)

        ctk.CTkButton(btns, text="Entrar", width=140, command=self.entrar).pack(side="left", padx=6)
        ctk.CTkButton(btns, text="Registrar novo", width=180, command=self._registrar).pack(side="left", padx=6)

    def entrar(self):
        prof = InfoDos_professores()
        email = self.email.get().strip().lower()
        senha = self.senha.get()
        if email in prof and prof[email]["senha"] == senha:
            prof_dicio = prof[email]
            prof = Professor.from_dict(prof_dicio)
            self.on_login(prof)
        else:
            messagebox.showerror("Erro", "Email ou senha incorretos.")

    def _registrar(self):
        win = ctk.CTkToplevel(self)
        win.title("Registrar Professor")
        win.geometry("480x380")
        win.configure(fg_color="#153b2f")

        frm = ctk.CTkFrame(win, fg_color="#1f6650")
        frm.pack(padx=12, pady=12, fill="both", expand=True)

        ctk.CTkLabel(frm, text="Nome:", text_color="#9cf4ae").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        nome = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); nome.grid(row=0, column=1, padx=6, pady=6)
        ctk.CTkLabel(frm, text="Idade:", text_color="#9cf4ae").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        idade = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); idade.grid(row=1, column=1, padx=6, pady=6, sticky="w")
        ctk.CTkLabel(frm, text="CPF:", text_color="#9cf4ae").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        cpf = ctk.CTkEntry(frm, width=200, fg_color="#3d7961"); cpf.grid(row=2, column=1, padx=6, pady=6, sticky="w")
        ctk.CTkLabel(frm, text="Email:", text_color="#9cf4ae").grid(row=3, column=0, sticky="w", padx=6, pady=6)
        email = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); email.grid(row=3, column=1, padx=6, pady=6)
        ctk.CTkLabel(frm, text="Senha:", text_color="#9cf4ae").grid(row=4, column=0, sticky="w", padx=6, pady=6)
        senha = ctk.CTkEntry(frm, width=240, show="*", fg_color="#3d7961"); senha.grid(row=4, column=1, padx=6, pady=6, sticky="w")

        def salvar():
            if not nome.get().strip() or not email.get().strip() or not senha.get().strip():
                messagebox.showwarning("Aviso", "Preencha nome, email e senha.")
                return
            prof = InfoDos_professores()
            emailInserido = email.get().strip().lower()
            if emailInserido in prof:
                messagebox.showwarning("Aviso", "Esse email já está cadastrado.")
                return
            prof[emailInserido] = {"nome": nome.get().strip(), "idade": int(idade.get() or 0), "CPF": cpf.get().strip(), "email": emailInserido, "senha": senha.get()}
            salvar_professores(prof)
            messagebox.showinfo("Sucesso", "Professor registrado.")
            win.destroy()

        ctk.CTkButton(frm, text="Salvar", command=salvar).grid(row=6, column=0, columnspan=2, pady=12)
