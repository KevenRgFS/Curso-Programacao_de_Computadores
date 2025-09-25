import csv

alunos = [
    {"nome": "Carlos", "nota":8.5}, 
    {"nome": "Sofia", "nota": 9.2}]

with open("alunos.csv", "w") as escola:

    dados = csv.writer(escola)
    dados.writerow(["nome", "nota"])
    for i in alunos:
        dados.writerow([i["nome"], i["nota"]])