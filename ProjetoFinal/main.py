import customtkinter as tk
from tkinter import messagebox, scrolledtext
from professor import Professor
from aluno import Aluno

def abrir_nova_janela(usuario):
    # Cria uma nova janela (filha)
    nova_janela = tk.CTkToplevel(root)
    nova_janela.title(f"Painel Administrativo do {usuario.capitalize()} - SUCE")
    nova_janela.geometry("900x700")
    nova_janela.configure(fg_color="#1b3b30")

    frame_busca_alunos = tk.CTkFrame(nova_janela, width=550, height=35, fg_color="#24996c")
    frame_busca_alunos.place(x=210, y=4)

    informativo = tk.CTkLabel(frame_busca_alunos, text="Busque um Aluno:", font=("Berlin Sans FB Demi", 18, "bold"), text_color="#9cf4ae")
    informativo.place(x=10, y=1.5)

    entrada_BA = tk.CTkEntry(frame_busca_alunos, width=370, fg_color="#ffffff")
    entrada_BA.place(x=165, y=2.2)
    

    botaoDEbusca = tk.CTkButton(nova_janela, text="Buscar", font=("Berlin Sans FB Demi", 19), corner_radius=5, fg_color="white", hover_color="grey", text_color="#24996c", width=100, height=35)
    botaoDEbusca.place(x=780, y=4)



def login_sistema():

    usuario = entrada_depto.get().strip().lower()
    senha = entrada_depto2.get().strip()

    if usuario in login and login[usuario]["senha"] == senha:
        messagebox.showinfo("Login Bem Sucedido", f"Bem Vindo, {usuario.capitalize()}")
        abrir_nova_janela(usuario)
    else:
        messagebox.showerror("Login Mal Sucedido", "Credenciadas incorretas, tente novamente!")

login = {

    "thiago": {"senha": "1234"},
    "jessica": {"senha": "4321"},
    "k": {"senha": "k"}
}

#aluno1 = Aluno("Ana", 18, 75757575, 214587, "Programação de Computadores", 4)
#Professor1 = Professor("Igor", 32, 74747474, "POO", "ADS")

#print(aluno1.descricao())
#print(Professor1.descricao())


#Aluno.AddA()
#Professor.descricaoA()

# Janela principal
tk.set_appearance_mode("Light")  # ou "Light" ou "Dark"
tk.set_default_color_theme("green")

root = tk.CTk(fg_color="#24996c")
root.title("Sistema Unificado de Controle Educacional - SUCE", )
root.geometry("500x400")

titulo = tk.CTkLabel(root, text="Login para Docentes", font=("Berlin Sans FB Demi", 35, "bold"), text_color="white")
titulo.pack(pady=40)

# Campo de busca

frame_busca = tk.CTkFrame(root, fg_color="#24996c")
frame_busca.pack(pady=10)

frame_busca2 = tk.CTkFrame(root, fg_color="#24996c")
frame_busca2.pack(pady=11)

label_depto = tk.CTkLabel(frame_busca, text="Matrícula ou Nome:", font=("Berlin Sans FB Demi", 20, "underline"), text_color="#9cf4ae")
label_depto.pack(side="top", padx=5)

entrada_depto = tk.CTkEntry(frame_busca, width=200, fg_color="#3d7961")
entrada_depto.pack(side="left", padx=5)

label_depto2 = tk.CTkLabel(frame_busca2, text="Senha:", font=("Berlin Sans FB Demi", 20, "underline"), text_color="#9cf4ae")
label_depto2.pack(side="top", padx=5)

entrada_depto2 = tk.CTkEntry(frame_busca2, width=200, fg_color="#3d7961")
entrada_depto2.pack(side="left", padx=5)

# Botões

frame_botoes = tk.CTkFrame(root, fg_color="#24996c")
frame_botoes.pack(pady=10)

Entrar = tk.CTkButton(frame_botoes, text="Entrar", font=("Berlin Sans FB Demi", 19), corner_radius=10, fg_color="white", hover_color="grey", text_color="#24996c", width=220, command= login_sistema)
Entrar.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()