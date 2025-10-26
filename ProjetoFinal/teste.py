import customtkinter as tk
from tkinter import messagebox, scrolledtext

# Dados simulados
dados_funcionarios = [
    {"nome": "Gustavo", "vendas": 74355, "anos_experiencia": 4, "departamento": "Vendas"},
    {"nome": "Bruno", "vendas": 46826, "anos_experiencia": 5, "departamento": "Marketing"},
    {"nome": "Estelar", "vendas": 90750, "anos_experiencia": 6, "departamento": "Vendas"},
    {"nome": "Ana", "vendas": 32000, "anos_experiencia": 2, "departamento": "RH"}
]

# Funções
def aplicar_bonus():
    resultado_text.delete("1.0", "end")
    resultado_text.insert("end", "--- 4. APLICAÇÃO DE BÔNUS ---\n")
    contador_bonus = 0
    for f in dados_funcionarios:
        if f["anos_experiencia"] > 3:
            bonus = f["vendas"] * 0.10
            f["vendas"] += bonus
            resultado_text.insert("end", f"Bônus aplicado a {f['nome']}. Novas Vendas: R$ {f['vendas']:.2f}\n")
            contador_bonus += 1
    resultado_text.insert("end", f"\nProcesso de bônus concluído. Total de {contador_bonus} bônus aplicados.\n")
    messagebox.showinfo("Bônus Aplicado", "Bônus de 10% aplicado para funcionários com mais de 3 anos de experiência.")

def listar_todos():
    resultado_text.delete("1.0", "end")
    resultado_text.insert("end", "--- LISTAGEM DE FUNCIONÁRIOS ---\n")
    for f in dados_funcionarios:
        resultado_text.insert("end", f"{f['nome']} - Vendas: R$ {f['vendas']:.2f} - Experiência: {f['anos_experiencia']} anos - Departamento: {f['departamento']}\n")

def media_vendas():
    media = sum(f["vendas"] for f in dados_funcionarios) / len(dados_funcionarios)
    messagebox.showinfo("Média de Vendas", f"Média geral de vendas: R$ {media:.2f}")

def melhor_desempenho():
    melhor = max(dados_funcionarios, key=lambda x: x["vendas"])
    messagebox.showinfo("Melhor Desempenho", f"Melhor desempenho: {melhor['nome']} com R$ {melhor['vendas']:.2f}")

def consultar_por_departamento():
    depto = entrada_depto.get()
    resultado_text.delete("1.0", "end")
    resultado_text.insert("end", f"--- Funcionários do Departamento: {depto} ---\n")
    encontrados = [f for f in dados_funcionarios if f["departamento"].lower() == depto.lower()]
    
    if encontrados:
        for f in encontrados:
            resultado_text.insert("end", f"{f['nome']} - Vendas: R$ {f['vendas']:.2f} - Experiência: {f['anos_experiencia']} anos\n")
    else:
        resultado_text.insert("end", "Nenhum funcionário encontrado neste departamento.\n")

# Janela principal
tk.set_appearance_mode("Light")  # ou "Light" ou "Dark"
tk.set_default_color_theme("blue")

root = tk.CTk()
root.title("Painel de Análise de Desempenho (SAR-G)")
root.geometry("800x600")

# Campo de busca
frame_busca = tk.CTkFrame(root)
frame_busca.pack(pady=10)

label_depto = tk.CTkLabel(frame_busca, text="Departamento para Consultar:")
label_depto.pack(side="left", padx=5)

entrada_depto = tk.CTkEntry(frame_busca, width=200)
entrada_depto.pack(side="left", padx=5)

btn_buscar = tk.CTkButton(frame_busca, text="1. Consultar por Depto", corner_radius=0, command=consultar_por_departamento)
btn_buscar.pack(side="left", padx=5)

# Título
titulo = tk.CTkLabel(root, text="Controle de Dados da Equipe", font=("Arial", 20, "bold"))
titulo.pack(pady=10)

# Botões
frame_botoes = tk.CTkFrame(root)
frame_botoes.pack(pady=10)

btn2 = tk.CTkButton(frame_botoes, text="2. Média Geral de Vendas", corner_radius=0, fg_color="white", hover_color="light gray", text_color="black", width=220, command=media_vendas)
btn2.grid(row=0, column=0, padx=10, pady=5)

btn3 = tk.CTkButton(frame_botoes, text="3. Melhor Desempenho", corner_radius=0, fg_color="white", hover_color="light gray", text_color="black", width=220, command=melhor_desempenho)
btn3.grid(row=0, column=1, padx=10, pady=5)

btn4 = tk.CTkButton(frame_botoes, text="4. Aplicar Bônus (+10%)", corner_radius=0, fg_color="white", hover_color="light gray", text_color="black", width=220, command=aplicar_bonus)
btn4.grid(row=1, column=0, padx=10, pady=5)

btn5 = tk.CTkButton(frame_botoes, text="5. Listar Todos os Registros", corner_radius=0, fg_color="white", hover_color="light gray", text_color="black", width=220, command=listar_todos)
btn5.grid(row=1, column=1, padx=10, pady=5)

btn_sair = tk.CTkButton(frame_botoes, text="SAIR", fg_color="red", corner_radius=0, hover_color="darkred", command=root.quit, width=220)
btn_sair.grid(row=2, column=0, columnspan=2, pady=10)

# Área de texto
resultado_text = scrolledtext.ScrolledText(root, width=87, height=20)
resultado_text.pack(pady=10)

root.mainloop()