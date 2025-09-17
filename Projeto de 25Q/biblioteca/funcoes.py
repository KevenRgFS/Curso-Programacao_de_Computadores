def contar_vogais():

    print("Vamos contar vogais!\n")
    vogais = "aeiouáéíóôú"
    palavra = input("Declare sua palavra: ")

    contador = 0

    for letra in palavra:
        if letra in vogais:
            contador+=1
    

    print(f"\nSua palavra tem: {contador} vogais")

def tabuadaI():

    print("Vamos montar sua tabuada!\n")
    numero = int(input("Declare seu número: "))

    for i in range(11):

        print(f"{numero} x {i} =", i*numero)

def Senha_tentativas():

    print("Vamos tentar sua senha!\n")
    senha = "senha"

    tentativa = 0

    while tentativa < 3:

        tente = input("Senha: ")

        if(tente == senha):
            print("Bem vindo!")
            break
        else:
            print("Senha incorreta!")
            tentativa+=1
        
        if(tentativa==3):
            print("Tentativas excedentes! Sistema bloqueado.")

def Soma_pares():

    print("Vamos somar os pares até 100!\n")
    aux = 0

    for i in range(0, 101, 2):
    
        aux += i
    

    print("A soma dos pares até 100 é:", aux)

def Adivinhar_numero():
    
    print("Vamos brincar de adivinhação!\n")
    import random

    num = random.randint(1,100)
    contador = 0

    while contador < 10:

        tentativa = int(input("Chute um número: "))

        if(tentativa > num):
            print("Chute mais baixo :)\n")
        elif(tentativa < num):
            print("Chute mais alto :)\n")
        else:
            print("Aeeee, você acertou!!! ;3\n")
            break

        contador+=1

        if(contador == 10):
            print("\nTentativas excedentes! Você perdeu :(")
            print("O número era:", num)
            break

def fibonacci():

    print("Vamos ver a sequência de Fibonacci!\n")
    n = int(input("Quantos termos da sequência você quer ver? "))

    num1, num2 = 0, 1
    contador = 0

    print("Sequência de Fibonacci:")

    while contador < n:
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2
        contador += 1

def Lista_compra():

    print("Vamos atualizar sua lista de compras!\n")
    print("Lista de Compras:")

    lista = []

    opcao = 0

    while opcao != 3:

        print("--MENU--\n")
        print("1- adicionar item\n 2- excluir item\n 3- fechar lista")
        opcao = int(input("Declare sua opção: "))

        if(opcao == 1):
            add = input("\nQual o item: ")
            lista.append(add)
            print("\nLista atualizada:\n", lista)
            print("\n")

        elif(opcao == 2):
            exc = input("\nQual item: ")
            lista.remove(exc)
            print("\nLista atualizada:\n", lista)
            print("\n")

        elif(opcao == 3):
            print("\nLista fechada!\n")
            break


    print("Lista de Compras:\n")
    for compras in lista:
    
        print(compras)

def Verificar_primo():

    print("Vamos ver se seus números são primos!\n")
    num = int(input("Declare o número que deseja verificar: "))

    if(num<2):
        print("Seu número não é primo")

    else:

        for i in range(2, int(num/2) +1):
            if(num%i==0):
                print("Seu número não primo!")
                break
            else:
                print("Seu número é primo")

def Calculadora():

    print("Vamos calcular algo simples!\n")
    print("--MENU--\n")

    num1 = float(input("Declare o primeiro número: "))
    num2 = float(input("Declare o segundo número: "))

    print("Declare sua operação:\n")
    opcao = input("1- +\n 2- -\n 3- *\n 4- /\n Aqui: ")

    soma = num1+num2
    subt = num1-num2
    mult = num1*num2
    div = num1/num2

    if(opcao == '+' or opcao == "1"):
        print(f"\n{num1} + {num2} =", soma)

    elif(opcao == '-' or opcao == "2"):
        print(f"\n{num1} - {num2} =", subt)

    elif(opcao == '*' or opcao == "3"):
        print(f"\n{num1} x {num2} =", mult)

    elif(opcao == '/' or opcao == "4"):
        print(f"\n{num1} / {num2} =", div)

def Contagem_regressiva():

    print("Vamos fazer uma contagem regressiva!\n")
    num = int(input("Declare o inicio da contagem: "))

    for i in range(num, -1, -1):
        print(i)

def Calcular_media():

    print("Vamos ver a média de seus números!\n")
    num = float(input("Declare o primeiro número que quer somar: "))

    soma=0 
    contador=0
    num2=1

    while num2 !=0:

        num2 = float(input("Próximo número(0 para encerrar):"))
        contador+=1
        soma += num2
        print(soma)

    media = (soma+num) / (contador)

    print(f"\nSua média é: {media:.2f}")

def tabuada():

    print("Vamos montar sua tabuada!\n")
    num = int(input("Declare o número que deseja ver a tabuada: "))

    contador = 0
    mult = 0

    while contador !=11:

        print(f"{num} x {contador} =", mult)
        contador+=1
        mult = contador*num

def Fatorial():

    print("Vamos mostrar o fatorial do seu número!\n")
    num = int(input("Declare o número que deseja ter o fatorial: "))

    fatorial = 1
    mult = num
    for i in range(num, 1, -1):

        fatorial *= i

    print(fatorial)

def Exibir_impar():

    print("Vamos ver os números impares?\n")
    i=1
    num = int(input("Declare o limite da sequencia: "))

    while i <= num:

        if(i%2 != 0):
            print(i)
        i+=1

    print("São números impares!")

def Somar_digitos():

    print("Vamos somar os algarismos do seu número?\n")
    num = int(input("Declare o número que deseja somar os algarismos: "))

    soma=0

    for i in str(num):

        soma += int(i)
    
    print("A soma deles é", soma)

def PA():

    print("Vamos montar uma PA!\n")
    a1 = int(input("Declare o primeiro termo: "))
    r = int(input("Declare a razão da PA: "))
    limi = int(input("Até onde quer ver sua sequência?: "))

    PA = []
    for i in range(0, limi+1):

        an = a1 + (i-1) * r
        PA.append(an)

    print(PA)

def Validar_email():

    print("Nos deixe verificar seu email.\n")
    email = input("Declare seu email: ")


    for i in email:

        if("@" in email and '.' in email):
            print("Seu email é válido")
            break
        else:
            print("Seu email não é válido!")
            break

def Contar_consoantes():

    print("Vamos contar as consoantes do seu número.\n")
    consoantes = ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    contador_conso = 0

    texto = input("Escreva seu texto abaixo:\n")

    for i in texto:
        if i in consoantes:
            contador_conso+=1

    print(f"Seu texto tem {contador_conso} consoantes.")

def jogo_forca():

    import random

    print("Vamos jogar forca?\n")
    palavras = ["maça", "banana", "tomate", "uva", "pitaya", "abacaxi", "maracuja", "caju", "mamão", "tangerina"]
    palavra = random.choice(palavras).lower()

    descobertas = ["_"] * len(palavra)
    tentativas_max = 6
    erros = 0
    letras_chutadas = set()

    print("\t--- Jogo da Forca ---")
    print("\tEdição: frutas")
    print("Chute uma letra ou a palavra interira")
    print(f"Você tem {tentativas_max} erros permitidos.\n")

    while erros < tentativas_max and "_" in descobertas:
        print("Palavra:", " ".join(descobertas))
        print("Letras chutadas:", " ".join(sorted(letras_chutadas)) if letras_chutadas else "(nenhuma)")
        chute = input("Digite uma letra ou chute a palavra inteira: ").strip().lower()

        if not chute:
            print("Entrada vazia. Tente novamente.\n")
            continue

        if len(chute) > 1:
            if chute == palavra:
                descobertas = list(palavra)
                break
            else:
                erros += 1
                print(f"Palavra incorreta! Erros: {erros}/{tentativas_max}\n")
                continue

        letra = chute[0]
        if not letra.isalpha():
            print("Declare apenas letras.\n")
            continue

        if letra in letras_chutadas:
            print("Você já chutou essa letra. Tente outra.\n")
            continue

        letras_chutadas.add(letra)

        if letra in palavra:
            for i, c in enumerate(palavra):
                if c == letra:
                    descobertas[i] = letra
            print("Acertou a letra!\n")
        else:
            erros += 1
            print(f"Errou! Erros: {erros}/{tentativas_max}\n")


    if "_" not in descobertas:
        print("Parabéns! Você descobriu a palavra:", palavra)
    else:
        print("Você perdeu! A palavra era:", palavra)



def multip_russa():

    a = int(input("Digite o primeiro número: "))
    b = int(input("Digite o segundo número: "))

    resultado = 0

    print("\nPassos da multiplicação russa:")
    while a > 0:
        print(f"{a}\t{b}", end="")

        if a % 2 != 0:
            resultado += b
            print(f"  -> soma {b}")
        else:
            print()
        a //= 2 
        b *= 2

    print("\nResultado final: ", resultado)


def Collatz():

    n = int(input("Declare um número inteiro positivo: "))

    print("Sequência de Collatz:")
    print(n, end=" ")

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n, end=" ")

def palindromo():

    print("Vamos ver sua palavra é igual de trás para frente?\n")
    palavra = input("Digite uma palavra: ").lower().replace(" ", "")

    sim_palindromo = True
    tamanho = len(palavra)

    for i in range(tamanho // 2):
        if palavra[i] != palavra[tamanho - 1 - i]:
            sim_palindromo = False
            break

    if sim_palindromo:
        print("É palíndromo!")
    else:
        print("Não é palíndromo!")

def banco():

    print("Vamos trabalhar com a sua conta no banco EFGSK!\n")
    saldo = 0.0

    while True:
        print("\n---BANCO EFGSK---")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"Seu saldo atual é: R$ {saldo:.2f}")

        elif opcao == "2":
            valor = float(input("Digite o valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Valor inválido para depósito.")

        elif opcao == "3":
            valor = float(input("Digite o valor para saque: R$ "))
            if valor > 0:  
                if valor <= saldo:
                    saldo -= valor
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Valor inválido para saque.")

        elif opcao == "4":
            print("Saindo do sistema... Obrigado por usar o Banco EFGSK!")
            break

        else:
            print("Opção inválida, tente novamente.")

def Contador_inteligente():

    try:
        n = int(input("Digite um número inteiro positivo: "))

        if n < 0:
            print("Erro: número negativo não é permitido.")
        else:
            soma = 0
            for i in range(1, n + 1):
                soma += i
            print(f"A soma dos números de 1 até {n} é {soma}")

    except ValueError:
        print("Erro: você deve digitar apenas números inteiros.")