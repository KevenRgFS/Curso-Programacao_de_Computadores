PI = 3.14
opcao = 99999
import math

def rendimento(area):

    rendi = area/0.0045
    print(f"\n-- Será preciso {rendi:.2f}ml de tinta para cobrir a área.\n")

def preco(area):

    QuantLata = area/81

    if QuantLata <=1:
        print("-- Você terá que comprar 1 lata, no valor de R$799,92\n")
    elif QuantLata.is_integer():
        QuantInteiro = int(QuantLata)
        preco = QuantInteiro*799.92
        print(f"-- Você terá que comprar {QuantInteiro} latas, no valor de R${preco:.2f}\n")
    else:
        QuantInteiro = math.ceil(QuantLata)
        preco = QuantInteiro*799.92
        print(f"-- Você terá que comprar {QuantInteiro} latas, no valor de R${preco:.2f}\n")


while opcao != 0:

    print("0- Sair\n1- Quadrado.\n2- Trapézio.\n3- Retangulo.\n4- Triângulo.\n5- Losango\n6- Circunferência.\n")
    opcao = int(input("De qual figura você deseja calcular a área?\n"))

    if opcao == 0:
        print("Programa fechado!")
        break

    elif opcao == 1:

        print("Declare o valor dos lados(em metros) do seu espaço:")
        l1 = float(input("1° lado: "))
        l2 = float(input("2° lado: "))

        #cm1 = l1*100
        #cm2 = l2*100

        areaQua= l1*l2
        

        print(f"\n-- A área do seu quadrado (em metros quadrados) é: {areaQua:.2f}m^2")
        rendimento(areaQua)
        preco(areaQua)

    elif opcao == 2:

        print("Declare o valor das bases e da altura(em metros) do seu espaço:")
        b1 = float(input("Base maior: "))
        b2 = float(input("Base menor: "))
        h = float(input("Altura: "))


        #cm1 = b1*100
        #cm2 = b2*100
        #cm3= h*100

        areaTra= ((b1+b2)*h)/2
        

        print(f"\n-- A área do seu trapézio (em metros quadrados) é: {areaTra:.2f}m^2")
        rendimento(areaTra)
        preco(areaTra)

    
    elif opcao == 3:

        print("Declare o valor dos lados(em metros) do seu espaço:")
        l1 = float(input("1° lado: "))
        l2 = float(input("2° lado: "))

        #cm1 = l1*100
        #cm2 = l2*100

        areaRen= l1*l2
        

        print(f"\n-- A área do seu retângulo (em metros quadrados) é: {areaRen:.2f}m^2")
        rendimento(areaRen)
        preco(areaRen)

    elif opcao == 4:

        print("Declare o valor da base e da altura(em metros) do seu espaço:")
        l1 = float(input("Base: "))
        l2 = float(input("altura: "))

        #cm1 = l1*100
        #cm2 = l2*100

        areaTri= l1*l2/2
        

        print(f"\n-- A área do seu triângulo (em metros quadrados) é: {areaTri:.2f}m^2")
        rendimento(areaTri)
        preco(areaTri)

    elif opcao == 5:

        print("Declare o valor o valor das duas diagonais(em metros) do seu espaço:")
        l1 = float(input("1° Diagonal: "))
        l2 = float(input("2° Diagonal: "))

        #cm1 = l1*100
        #cm2 = l2*100

        areaLos= l1*l2/2
        

        print(f"\n-- A área do seu losango (em metros quadrados) é: {areaLos:.2f}m^2")
        rendimento(areaLos)
        preco(areaLos)

    elif opcao == 6:

        print("Declare o valor o valor do raio(em metros) do seu círculo:\n")
        r = float(input("Raio: "))

        #cm1 = r*100

        areaCir= PI*(r*r)

        print(f"\n-- A área da sua circunferência(em metros quadrados) é: {areaCir:.2f}m^2")
        rendimento(areaCir)
        preco(areaCir)
    else:
        print("Opção não existente! Tente novamente.\n")



