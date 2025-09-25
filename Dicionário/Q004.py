"""Dicionário de Dicionários: Crie um dicionário chamado
cidades_por_estado. As chaves do dicionário principal devem ser os
nomes de estados. Os valores devem ser outros dicionários, onde as
chaves são os nomes das cidades e os valores são o número de
habitantes.
o Adicione pelo menos 2 estados com 2 cidades cada.
o Imprima o número de habitantes de uma cidade específica, como
"Belo Horizonte"."""

cidades_por_estado = {

    "Pará": {

        "Marabá": "288.513",
        "Belém": "1.303.403"
        
    },

    "Goiás": {

        "Santo Antônio do Descoberto": "72.127",
        "Goiânia": "1.494.599"
    },

    "Tocantins": {

        "Almas": "6.483",
        "Palmas": "302.692"
    }
}


print("Cidades Disponíveis:\n\n- Marabá.\n- Belém.\n- Santo Antônio do Descoberto.\n- Goiânia.\n- Almas.\n- Palmas.\n")

cid = input("Declare a cidade que deseja saber o n° de habitantes:\n")

for estado, inf_cidade in cidades_por_estado.items():

    if cid in inf_cidade:

        num = inf_cidade[cid]
        #num = hab["Tocantins"{"Almas"}]

            #print(hab[])
        print(f"\n{cid} tem um número de {num} habitantes.")