from biblioteca import funcoes

escolha = 30

while escolha != 0:

    print("\n\n---MENU DE FUNÇÕES---\n")

    print("0- Para Sair\n1- Contar Vogais\n2- Tabuada Interativa.\n3- Senha com tentativas\n4- Soma de Pares\n5- Adivinhação\n6- Fibonacci\n7- Lista de Compras\n8- Verificador de Primo\n9- Calculadora Simples\n10- Contagem Regressiva\n11- Média\n12- Tabuada\n13- Fatorial\n14- Números Ímpares\n15- Soma Dígitos\n16- Progressão Aritmética\n17- Validador de Email\n18- Contador de Consoantes\n19- Jogo da Forca Simplificado\n20- Multiplicação Russa\n21- Sequência de Collatz\n22- Palíndromo\n23- Banco\n24- Contador Inteligente\n")
    
    try:
        escolha = int(input("Escolha o que quer fazer: "))
    except ValueError:
        print("Digite apenas números válidos.")
        continue

    print("\n")
    if escolha == 0:
        print("Encerrando programa...")
    elif escolha == 1:
        funcoes.contar_vogais()
    elif escolha == 2:
        funcoes.tabuadaI()
    elif escolha == 3:
        funcoes.Senha_tentativas()
    elif escolha == 4:
        funcoes.Soma_pares()
    elif escolha == 5:
        funcoes.Adivinhar_numero()
    elif escolha == 6:
        funcoes.fibonacci()
    elif escolha == 7:
        funcoes.Lista_compra()
    elif escolha == 8:
        funcoes.Verificar_primo()
    elif escolha == 9:
        funcoes.Calculadora()
    elif escolha == 10:
        funcoes.Contagem_regressiva()
    elif escolha == 11:
        funcoes.Calcular_media()
    elif escolha == 12:
        funcoes.tabuada()
    elif escolha == 13:
        funcoes.Fatorial()
    elif escolha == 14:
        funcoes.Exibir_impar()
    elif escolha == 15:
        funcoes.Somar_digitos()
    elif escolha == 16:
        funcoes.PA()
    elif escolha == 17:
        funcoes.Validar_email()
    elif escolha == 18:
        funcoes.Contar_consoantes()
    elif escolha == 19:
        funcoes.jogo_forca()
    elif escolha == 20:
        funcoes.multip_russa()
    elif escolha == 21:
        funcoes.Collatz()
    elif escolha == 22:
        funcoes.palindromo()
    elif escolha == 23:
        funcoes.banco()
    elif escolha == 24:
        funcoes.Contador_inteligente()