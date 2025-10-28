import customtkinter as tk
from tkinter import scrolledtext, messagebox

# Dicionário de alunos
alunos = {}

# Função adaptada da sua AddA()
def AddA():
    nome = entrada_nome.get().strip()
    idade = entrada_idade.get().strip()
    cpf = entrada_cpf.get().strip()
    matricula = entrada_matricula.get().strip()
    curso = entrada_curso.get().strip()
    semestre = entrada_semestre.get().strip()

    if not (nome and idade and cpf and matricula and curso and semestre):
        messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
        return

    matricula_formatada = "EFGa" + str(matricula)
    semestre_formatado = f"{semestre}°"

    alunos[nome] = {
        "Nome Completo": nome,
        "Idade": int(idade),
        "CPF": int(cpf),
        "Matrícula": matricula_formatada,
        "Curso": curso,
        "Semestre": semestre_formatado
    }

    # Mostra o aluno no ScrolledText
    texto.insert("end", f"\nAluno {nome} cadastrado com sucesso!\n")
    texto.insert("end", f"📘 Nome: {nome}\n🎓 Curso: {curso}\n🆔 Matrícula: {matricula_formatada}\n📅 Semestre: {semestre_formatado}\n")
    texto.insert("end", "--------------------------------------------\n")
    texto.see("end")  # rola para o final automaticamente

    # Limpa os campos
    entrada_nome.delete(0, "end")
    entrada_idade.delete(0, "end")
    entrada_cpf.delete(0, "end")
    entrada_matricula.delete(0, "end")
    entrada_curso.delete(0, "end")
    entrada_semestre.delete(0, "end")

# Interface gráfica
tk.set_appearance_mode("Light")
tk.set_default_color_theme("green")

root = tk.CTk()
root.geometry("800x600")
root.title("Cadastro de Alunos - SUCE")

frame_form = tk.CTkFrame(root)
frame_form.pack(pady=20, padx=20)

# Campos
entrada_nome = tk.CTkEntry(frame_form, placeholder_text="Nome Completo", width=300)
entrada_nome.grid(row=0, column=0, padx=10, pady=5)
entrada_idade = tk.CTkEntry(frame_form, placeholder_text="Idade", width=150)
entrada_idade.grid(row=0, column=1, padx=10, pady=5)
entrada_cpf = tk.CTkEntry(frame_form, placeholder_text="CPF", width=150)
entrada_cpf.grid(row=1, column=0, padx=10, pady=5)
entrada_matricula = tk.CTkEntry(frame_form, placeholder_text="ID Matrícula", width=150)
entrada_matricula.grid(row=1, column=1, padx=10, pady=5)
entrada_curso = tk.CTkEntry(frame_form, placeholder_text="Curso", width=300)
entrada_curso.grid(row=2, column=0, padx=10, pady=5)
entrada_semestre = tk.CTkEntry(frame_form, placeholder_text="Semestre", width=150)
entrada_semestre.grid(row=2, column=1, padx=10, pady=5)

# Botão de cadastrar
botao_add = tk.CTkButton(root, text="Cadastrar Aluno", command=AddA, width=200)
botao_add.pack(pady=15)

# Área de exibição (ScrolledText)
texto = scrolledtext.ScrolledText(root, width=80, height=15, wrap="word", bg="#e6ffee")
texto.pack(pady=20)

root.mainloop()
