import customtkinter as tk
from tkinter import scrolledtext

def pegar_nome():
    nome = entrada_nome.get("1.0", "end-1c").strip()
    if nome:
        label_resultado.configure(text=f"Olá, {nome.capitalize()}!")
    else:
        label_resultado.configure(text="Por favor, digite seu nome.")

tk.set_appearance_mode("Light")
tk.set_default_color_theme("green")

root = tk.CTk()
root.geometry("500x400")
root.title("Entrada com ScrolledText")

frame = tk.CTkFrame(root)
frame.pack(pady=40, padx=20)

label_titulo = tk.CTkLabel(frame, text="Digite seu nome:", font=("Berlin Sans FB Demi", 18))
label_titulo.pack(pady=10)

# ScrolledText padrão do tkinter (funciona dentro do customtkinter)
entrada_nome = scrolledtext.ScrolledText(frame, width=40, height=4, wrap="word", bg="#d6ffd6")
entrada_nome.pack(pady=10)

botao = tk.CTkButton(frame, text="Confirmar", command=pegar_nome)
botao.pack(pady=10)

label_resultado = tk.CTkLabel(frame, text="", font=("Berlin Sans FB Demi", 16), text_color="#24996c")
label_resultado.pack(pady=10)

root.mainloop()
