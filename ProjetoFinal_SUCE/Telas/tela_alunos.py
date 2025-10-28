import customtkinter as ctk
from tkinter import messagebox, scrolledtext
import json, os
from aluno import Aluno

BASE = os.path.join(os.path.dirname(__file__), "..", "Dados")
ALUNOS_FILE = os.path.join(BASE, "alunos.json")

def carregar_alunos():
    if not os.path.exists(ALUNOS_FILE):
        return {}
    with open(ALUNOS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_alunos(d):
    with open(ALUNOS_FILE, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=4, ensure_ascii=False)

class TelaAlunos(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(fg_color="#153b2f")
        self._build()

    def _build(self):
        top = ctk.CTkFrame(self, fg_color="#1f6650")
        top.pack(fill="x", pady=8, padx=8)
        ctk.CTkLabel(top, text="Gerenciar Alunos", font=("", 16, "bold"), text_color="#9cf4ae").pack(side="left", padx=8)

        btn_add = ctk.CTkButton(top, text="Adicionar Aluno", command=self._abrir_add)
        btn_add.pack(side="right", padx=8)

        # area central
        self.area = ctk.CTkFrame(self, fg_color="#153b2f")
        self.area.pack(fill="both", expand=True, padx=8, pady=8)
        self._listar()

    def _listar(self):
        for w in self.area.winfo_children():
            w.destroy()
        alunos = carregar_alunos()
        if not alunos:
            ctk.CTkLabel(self.area, text="Nenhum aluno cadastrado.", text_color="#9cf4ae").pack(padx=8, pady=8)
            return
        for chave, ad in alunos.items():
            fr = ctk.CTkFrame(self.area, fg_color="#1f6650")
            fr.pack(fill="x", padx=6, pady=6)
            ctk.CTkLabel(fr, text=f"{ad.get('nome')} ({ad.get('matricula')})", text_color="#9cf4ae").pack(side="left", padx=8)
            ctk.CTkButton(fr, text="Notas", width=80, command=lambda k=chave: self._notas(k)).pack(side="right", padx=6)
            ctk.CTkButton(fr, text="Ver", width=80, command=lambda k=chave: self._ver(k)).pack(side="right", padx=6)
            ctk.CTkButton(fr, text="Editar", width=80, command=lambda k=chave: self._editar(k)).pack(side="right", padx=6)
            ctk.CTkButton(fr, text="Remover", width=80, command=lambda k=chave: self._remover(k)).pack(side="right", padx=6)

    def _abrir_add(self):
        win = ctk.CTkToplevel(self)
        win.title("Adicionar Aluno")
        win.geometry("520x420")
        frm = ctk.CTkFrame(win, fg_color="#1f6650"); frm.pack(padx=12, pady=12, fill="both", expand=True)

        ctk.CTkLabel(frm, text="Nome:", text_color="#9cf4ae").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        nome = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); nome.grid(row=0, column=1, padx=6, pady=6)
        ctk.CTkLabel(frm, text="Idade:", text_color="#9cf4ae").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        idade = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); idade.grid(row=1, column=1, sticky="w", padx=6, pady=6)
        ctk.CTkLabel(frm, text="CPF:", text_color="#9cf4ae").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        cpf = ctk.CTkEntry(frm, width=200, fg_color="#3d7961"); cpf.grid(row=2, column=1, sticky="w", padx=6, pady=6)
        ctk.CTkLabel(frm, text="Matrícula:", text_color="#9cf4ae").grid(row=3, column=0, sticky="w", padx=6, pady=6)
        matricula = ctk.CTkEntry(frm, width=200, fg_color="#3d7961"); matricula.grid(row=3, column=1, sticky="w", padx=6, pady=6)
        ctk.CTkLabel(frm, text="Curso:", text_color="#9cf4ae").grid(row=4, column=0, sticky="w", padx=6, pady=6)
        curso = ctk.CTkEntry(frm, width=240, fg_color="#3d7961"); curso.grid(row=4, column=1, sticky="w", padx=6, pady=6)

        def salvar():
            if not nome.get().strip():
                messagebox.showwarning("Aviso", "Nome obrigatório"); return
            alunos = carregar_alunos()
            chave = f"aluno{len(alunos)+1}"
            a = Aluno(nome.get().strip(), int(idade.get() or 0), cpf.get().strip(), matricula.get().strip(), curso.get().strip(), "1°")
            alunos[chave] = a.dicionario()
            salvar_alunos(alunos)
            messagebox.showinfo("Sucesso", "Aluno cadastrado")
            win.destroy()
            self._listar()

        ctk.CTkButton(frm, text="Salvar", command=salvar).grid(row=8, column=0, columnspan=2, pady=12)

    def _ver(self, chave):
        alunos = carregar_alunos()
        ad = alunos.get(chave)
        if not ad:
            messagebox.showerror("Erro", "Aluno não encontrado"); return
        win = ctk.CTkToplevel(self)
        win.title("Detalhes do aluno")
        win.geometry("520x420")
        frm = ctk.CTkFrame(win, fg_color="#1f6650"); frm.pack(padx=12, pady=12, fill="both", expand=True)
        texto = ctk.CTkLabel(frm, text=f"Nome: {ad.get('nome')}\nMatrícula: {ad.get('matricula')}\nCurso: {ad.get('curso')}\nCPF: {ad.get('CPF')}", text_color="#9cf4ae", anchor="w", justify="left")
        texto.pack(padx=6, pady=6)

    def _editar(self, chave):
        alunos = carregar_alunos()
        ad = alunos.get(chave)
        if not ad:
            messagebox.showerror("Erro", "Aluno não encontrado"); return
        win = ctk.CTkToplevel(self)
        win.title("Editar Aluno")
        win.geometry("520x420")
        frm = ctk.CTkFrame(win, fg_color="#1f6650"); frm.pack(padx=12, pady=12, fill="both", expand=True)
        ctk.CTkLabel(frm, text="Nome:", text_color="#9cf4ae").grid(row=0, column=0, sticky="w", padx=6, pady=6)
        nome = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); nome.grid(row=0, column=1, padx=6, pady=6); nome.insert(0, ad.get('nome'))
        ctk.CTkLabel(frm, text="Curso:", text_color="#9cf4ae").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        curso = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); curso.grid(row=1, column=1, padx=6, pady=6); curso.insert(0, ad.get('curso'))
        ctk.CTkLabel(frm, text="CPF:", text_color="#9cf4ae").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        cpf = ctk.CTkEntry(frm, width=320, fg_color="#3d7961"); cpf.grid(row=2, column=1, padx=6, pady=6); cpf.insert(0, ad.get('CPF'))

        def salvar():
            ad['nome'] = nome.get().strip()
            ad['curso'] = curso.get().strip()
            ad['CPF'] = cpf.get().strip()
            salvar_alunos(alunos)
            messagebox.showinfo("Sucesso", "Aluno atualizado")
            win.destroy()
            self._listar()

        ctk.CTkButton(frm, text="Salvar", command=salvar).grid(row=8, column=0, columnspan=2, pady=12)

    def _remover(self, chave):
        alunos = carregar_alunos()
        if chave in alunos:
            if messagebox.askyesno("Confirmar", "Remover este aluno?"):
                del alunos[chave]
                salvar_alunos(alunos)
                self._listar()

    def _notas(self, chave):
        alunos = carregar_alunos()
        ad = alunos.get(chave)
        if not ad:
            messagebox.showerror("Erro", "Aluno não encontrado"); return

        notas = ad.get("notas", {"b1":0.0,"b2":0.0,"b3":0.0,"b4":0.0})
        win = ctk.CTkToplevel(self)
        win.title("Editar Notas")
        win.geometry("420x360")
        frm = ctk.CTkFrame(win, fg_color="#1f6650"); frm.pack(padx=12, pady=12, fill="both", expand=True)

        ctk.CTkLabel(frm, text=f"Notas de {ad.get('nome')}", text_color="#9cf4ae", font=("", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,8))

        ctk.CTkLabel(frm, text="Bimestre 1:", text_color="#9cf4ae").grid(row=1, column=0, sticky="w", padx=6, pady=6)
        b1 = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); b1.grid(row=1, column=1, padx=6, pady=6); b1.insert(0, str(notas.get('b1',0.0)))

        ctk.CTkLabel(frm, text="Bimestre 2:", text_color="#9cf4ae").grid(row=2, column=0, sticky="w", padx=6, pady=6)
        b2 = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); b2.grid(row=2, column=1, padx=6, pady=6); b2.insert(0, str(notas.get('b2',0.0)))

        ctk.CTkLabel(frm, text="Bimestre 3:", text_color="#9cf4ae").grid(row=3, column=0, sticky="w", padx=6, pady=6)
        b3 = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); b3.grid(row=3, column=1, padx=6, pady=6); b3.insert(0, str(notas.get('b3',0.0)))

        ctk.CTkLabel(frm, text="Bimestre 4:", text_color="#9cf4ae").grid(row=4, column=0, sticky="w", padx=6, pady=6)
        b4 = ctk.CTkEntry(frm, width=120, fg_color="#3d7961"); b4.grid(row=4, column=1, padx=6, pady=6); b4.insert(0, str(notas.get('b4',0.0)))

        def salvar_notas():
            try:
                nb1 = float(b1.get() or 0.0)
                nb2 = float(b2.get() or 0.0)
                nb3 = float(b3.get() or 0.0)
                nb4 = float(b4.get() or 0.0)
            except ValueError:
                messagebox.showwarning("Aviso", "Notas devem ser números."); return
            ad['notas'] = {'b1': nb1, 'b2': nb2, 'b3': nb3, 'b4': nb4}
            salvar_alunos(alunos)
            messagebox.showinfo("Sucesso", "Notas salvas.")
            win.destroy()

        ctk.CTkButton(frm, text="Salvar Notas", command=salvar_notas).grid(row=6, column=0, columnspan=2, pady=12)
