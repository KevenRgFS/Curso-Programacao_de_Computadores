"""import csv
# Escrita de arquivo CSV
with open("dados.csv", "w", newline="") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["nome", "idade", "cidade"]) # Cabeçalho
    escritor.writerow(["Ana", 25, "Lisboa"])
    escritor.writerow(["Pedro", 32, "Porto"])"""

import csv
# eitura de arquivo CSV
with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
