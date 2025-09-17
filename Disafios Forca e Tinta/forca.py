import random

def jogo_forca():
    print("Vamos jogar forca?\n")

    tentativas_max = 6
    erros = 0
    letras_chutadas = set()
    palavra = ""

    print("\t--- Jogo da Forca ---")
    print("Chute uma letra ou a palavra inteira")
    print(f"Você tem {tentativas_max} erros permitidos.\n")

    while True:
        print("\nCategorias:\n1- Jogos\n2- Filmes (Marvel/DC)\n3- Carros\n4- Artistas\n5- Frutas\n0- Sair\n")
        opcao = int(input("Escolha uma categoria: "))

        if opcao == 1:
            palavras = ["The Last of Us", "Omori", "Life is Strange", "The Witcher", "Red Dead Redemption", "Minecraft", "Hollow Knight"]
        elif opcao == 2:
            palavras = ["Ultimato", "O Contrato de Judas", "Guardiões da Galáxia", "Guerra de Apokolipse", "Thunderbolts", "A Morte do Superman", "Era de Ultron"]
        elif opcao == 3:
            palavras = ["Celta", "Corolla Cross", "Peugeot 208", "Brasilia", "Versa", "Haval", "Fusca"]
        elif opcao == 4:
            palavras = ["Angelina Jolie", "Cristiano Ronaldo", "Marília Mendonça", "Ana Paula Arosio", "Chico Buarque", "Djavan"]
        elif opcao == 5:
            palavras = ["maçã", "banana", "tomate", "uva", "pitaya", "abacaxi", "maracujá", "caju", "mamão", "tangerina"]
        elif opcao == 0:
            print("Saindo do Jogo!")
            return
        else:
            print("Opção inválida, tente novamente!\n")
            continue

        palavra = random.choice(palavras).lower()
        break

    descobertas = [" " if c == " " else "_" for c in palavra]

    while erros < tentativas_max and "_" in descobertas:
        print("\nPalavra:", " ".join(descobertas))
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
            print("Digite apenas letras.\n")
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


jogo_forca()
