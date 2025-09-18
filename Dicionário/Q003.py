"""Filtragem de Dados: Utilizando a lista de dicionários do exercício 1,
escreva um programa que percorra a lista e imprima o nome de todos os
participantes de eventos da modalidade "Corrida"."""

eventos_esportivos = [

    {
        "nome": "Dia do Esporte",
        "modalidade": "Fotebol",
        "participantes": ["6° ano", "8° ano", "9° ano", "3° série-EM"]
    },

    {
        "nome": "Campeonato InterEscola",
        "modalidade": "Vôlei",
        "participantes": ["CEPI José de Assis", "Colégio Estadual Salomão Elias Abdon", "Colégio Padrão"]
    },

    {
        "nome": "Maratona de SADE",
        "modalidade": "Maratona 25km",
        "participantes": ["Beatriz Evangelista", "Gabriella Braga", "João Henrique", "Lucas Domingues", "Laura Mavalli", "Marcos Uchoa"]
    }
]

print("Eventos agendados:\n")
for j in eventos_esportivos:
    print(j["nome"])
    

print("\n")
evento = input("De qual evento esportivo você deseja ver os participantes?\n")



for i in eventos_esportivos:

    if i["nome"] == evento:

        print("\nOs participantes são:\n", i["participantes"])