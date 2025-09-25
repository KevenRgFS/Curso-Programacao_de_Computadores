opcao = 99999


with open("diario.txt", "a") as hj:

    while opcao !=0:

        print("Bem vindo ao seu diário pessoal!\nO que deseja fazer:")
        print("1- Abrir uma entrada.\n2- Ler um dia.")

        opcao = int(input("1 ou 2: "))

        if opcao == 1:

            data = input("Declare a data(com '/' entre os números): ")

            texto = input("texto aqui:\n")

            with open("diario.txt", "a") as hj:

                hj.write(f"DATA: {data}\n{texto}\n---\n")

        elif opcao == 2:

            busca = input("Declare qual data quer ver(Com '/' entre os números): ")
            
            with open("diario.txt", "r") as info:
                busca