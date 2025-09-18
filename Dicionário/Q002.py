"""Consulta de Estoque: Você tem um dicionário chamado estoque. As
chaves são os nomes de produtos e os valores são dicionários com as
informações "quantidade" e "preco". Crie um programa que faça o
seguinte:
o Adicione um novo produto ao estoque.
o Verifique se um produto específico (ex: "maçã") existe no estoque
e imprima sua quantidade."""

def Add():

        prod = input("\nQual seria o produto?\n")
        quant = int(input("Teriamos quanto desse produto em estoque?\n"))
        preco = float(input("Quanto custaria esse produto?\n"))

        estoque[prod] = {
            "quantidade": quant,
            "preço": preco
        }

        print(f"{prod} adicionado ao estoque!")
        print(estoque[prod])
        print("\n")

def Buscar():

        prod = input("\nDeclare o produto que deseja buscar ou vizualizar:\n")

        if prod in estoque:
                
            print("Aqui está seu produto:\n")
            print(f"{prod}:")
            print(estoque[prod])
            print("\n")

        else:
            print("Não foram encontrados produtos correspondentes!")


estoque = {    
    
    "vaso":  
    {

    "quantidade": 20,
    "preço": "R$16.40"
    },

    "panela": {

        "quantidade": 15,
        "preço": "R$79.99"
    },

    "garrafa": {

        "quantidade": 31,
        "preço": "R$34.00"
    }
}

opcao = 9999
while opcao != 0:

    opcao = int(input("\nO que deseja fazer:\n1- Adicionar produto.\n2- Buscar/vizualizar produto.\n3- Visualizar estoque.\n0-sair.\n"))

    if opcao == 1:

        Add()

    elif opcao == 2:

        Buscar()

    elif opcao == 3:

        print("Aqui está seu estoque completo:")
        for i in estoque:
            print(i)

    elif opcao == 0:

        print("Fechando aba de estoque... ... ...\nEncerrado!")
