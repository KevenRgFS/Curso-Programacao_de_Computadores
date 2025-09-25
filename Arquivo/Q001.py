

with open("meus_dados.txt", "w") as backup:

    nome = input("Declare seu nome para registro:\n")
    idade = int(input("Declare sua idade para registro:\n"))
    
    backup.write("Registro de Voluntários:\n\n")
    backup.write(f"Nome: {nome}\n")
    backup.write(f"Idade: {idade} anos")
    
print("Informações armazenadas no banco de dados!")