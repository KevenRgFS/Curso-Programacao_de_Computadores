import customtkinter as tk
from tkinter import messagebox, scrolledtext
from professor import Professor
from aluno import Aluno


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
root.geometry("900x700")

titulo = tk.CTkLabel(root, text="Login para Docentes", font=("Berlin Sans FB Demi", 35, "bold"), text_color="white")
titulo.pack(pady=140)

# Campo de busca

frame_busca = tk.CTkFrame(root, fg_color="#24996c")
frame_busca.pack(pady=100)

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

Entrar = tk.CTkButton(frame_botoes, text="Entrar", font=("Berlin Sans FB Demi", 19), corner_radius=10, fg_color="white", hover_color="grey", text_color="#24996c", width=220)
Entrar.grid(row=5, column=0, padx=5, pady=5)
root.mainloop()