import json


def add():

    with open("Hab_city.json", "r") as info:

        conteudo = json.load(info)

    conteudo["Ceará"] ={
         
         "fortaleza": "2,578,483"
    }

    with open("Hab_city.json", "w", encoding="utf-8") as info:

        json.dump(conteudo, info, indent=4)

        print("\nConteúdo novo adicionado ao arquivo:")

        print(f"{conteudo}\n")

def ler():

        with open("Hab_city.json", "r") as info:

            kk = json.load(info)

            print(f"\n{kk}\n")

cidades_por_estado = {

    "Pará": {

        "Marabá": "288,513",
        "Belém": "1,303,403"
        
    },

    "Goiás": {

        "Santo Antônio do Descoberto": "72,127",
        "Goiânia": "1,494,599"
    },

    "Tocantins": {

        "Almas": "6,483",
        "Palmas": "302,692"
    }
}

with open("Hab_city.json", "w", encoding="utf-8") as info:

    json.dump(cidades_por_estado, info, indent=4)

    print("Seu arquivo de habitantes por cidade, foi salvo no dispositivo.\n")

opcao = 1
while opcao == 1 or opcao == 2:
    opcao = int(input("Se deseja ler o arquivo tecle 1\nSe deseja adicionar Ceará, tecle 2.\nopção: "))


    if opcao == 1:

        ler()
    elif opcao == 2:

        add()
    else:
     
        print("Opção inválida, encerrando atividade.")