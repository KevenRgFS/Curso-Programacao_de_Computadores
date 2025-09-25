with open("meus_dados.txt", "r") as backup:
    conteudo = backup.readlines()
    #print("Conteúdo do arquivo:\n")
    print(f"{conteudo[2]}{conteudo[3]}")
    