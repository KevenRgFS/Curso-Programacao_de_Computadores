import customtkinter as tk
from tkinter import messagebox

# ==========================
# Configuração principal
# ==========================

tk.set_appearance_mode("Light")  # "Dark" também funciona
tk.set_default_color_theme("green")

root = tk.CTk(fg_color="#24996c")
root.title("Sistema Unificado de Controle Educacional - SUCE")
root.geometry("900x700")

titulo = tk.CTkLabel(root, text="Login para Docentes", font=("Berlin Sans FB Demi", 35, "bold"), text_color="white")
titulo.pack(pady=100)

# ==========================
# Dados de login (simulação de "banco de dados")
# ==========================
usuarios = {
    "igor": {"senha": "1234", "cargo": "professor"},
    "ana": {"senha": "abcd", "cargo": "coordenadora"},
    "admin": {"senha": "admin", "cargo": "administrador"}
}

# ==========================
# Função para abrir nova janela
# ==========================
def abrir_painel(usuario):
    nova_janela = tk.CTkToplevel(root)
    nova_janela.title(f"Painel do {usuario.capitalize()} - SUCE")
    nova_janela.geometry("800x600")
    nova_janela.configure(fg_color="#1b3b30")

    titulo2 = tk.CTkLabel(
        nova_janela,
        text=f"Bem-vindo, {usuario.capitalize()}!",
        font=("Berlin Sans FB Demi", 30, "bold"),
        text_color="white"
    )
    titulo2.pack(pady=50)

    texto = tk.CTkLabel(
        nova_janela,
        text="Agora você está dentro do sistema.\nAqui pode gerenciar alunos, professores, relatórios e muito mais.",
        font=("Arial", 18),
        text_color="#b6e3c4",
        justify="center"
    )
    texto.pack(pady=20)

    tk.CTkButton(
        nova_janela,
        text="Sair",
        fg_color="#ff6666",
        hover_color="#cc0000",
        width=150,
        command=nova_janela.destroy
    ).pack(pady=30)

# ==========================
# Função de validação do login
# ==========================
def verificar_login():
    nome = entrada_depto.get().strip().lower()
    senha = entrada_depto2.get().strip()

    if nome in usuarios and usuarios[nome]["senha"] == senha:
        messagebox.showinfo("Login bem-sucedido", f"Bem-vindo(a), {nome.capitalize()}!")
        abrir_painel(nome)
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha incorretos.\nTente novamente.")

# ==========================
# Campos de entrada
# ==========================
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

entrada_depto2 = tk.CTkEntry(frame_busca2, width=200, fg_color="#3d7961", show="*")
entrada_depto2.pack(side="left", padx=5)

# ==========================
# Botão "Entrar"
# ==========================
frame_botoes = tk.CTkFrame(root, fg_color="#24996c")
frame_botoes.pack(pady=10)

Entrar = tk.CTkButton(
    frame_botoes,
    text="Entrar",
    font=("Berlin Sans FB Demi", 19),
    corner_radius=10,
    fg_color="white",
    hover_color="grey",
    text_color="#24996c",
    width=220,
    command=verificar_login  # 👈 agora chama a função de login
)
Entrar.grid(row=5, column=0, padx=5, pady=5)

root.mainloop()
