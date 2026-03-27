import random
 
 
while True:
    try:
        numero_secreto = random.randrange(10,101)
        chances_facil = 20
        chances_medio = 10
        chances_dificil = 5
        pontos = 100
 
        print(30*"-")
        print(" ADIVINHE O NÚMERO SECRETO ")
        print(30*"-")
 
        #print(f"Número Secreto: {numero_secreto}\n")
        nivel = input("Escolha um nível [fácil] [médio] [difícil]: ").lower()
        if nivel in ["fácil", "facil", "f"]:
                while chances_facil > 0:
                    print("\n[Você tem 20 chances]")
                    for i in range(chances_facil):
                        palpite = int(input("Informe seu palpite (entre 10 e 100): "))
                        if palpite < 10 or palpite > 100:
                                print("VOCÊ ERROU! Digite um número entre 10 e 100")
                                pontos -= 2
                                print(f"Pontuação: {pontos}\n")
                        elif palpite < numero_secreto:
                            print(30*"-","\nVocê errou! seu palpite é menor que o número secreto.")
                            pontos -= 2
                            print(f"Pontuação: {pontos}\n")
                        elif palpite > numero_secreto:
                            print(30*"-","\nVocê errou! seu palpite é maior que o número secreto.")
                            pontos -= 2
                            print(f"Pontuação: {pontos}\n")
                        elif palpite == numero_secreto:
                            print("Você acertou!")
                            pontos += 5
                            print(f"[ Pontuação Final: {pontos} ]")
                            break
                        else:
                            print("PALPITE INVÁLIDO! TENTE NOVAMENTE\n")
                    chances_facil -= 1
                    break
        elif nivel in ["médio", "medio", "m"]:
            while chances_medio > 0:
                print("\n[Você tem 10 chances]")
                for i in range(chances_medio):
                    palpite = int(input("Informe seu palpite (entre 10 e 100): "))
                    if palpite < 10 or palpite > 100:
                            print(30*"-","\nVOCÊ ERROU. Digite um número entre 10 e 100")
                            pontos -= 5
                            print(f"Pontuação: {pontos}\n")
 
                    elif palpite < numero_secreto:
                        print(30*"-","\nVocê errou! seu palpite é menor que o número secreto.")
                        pontos -= 5
                        print(f"Pontuação: {pontos}\n")
 
                    elif palpite > numero_secreto:
                        print(30*"-","\nVocê errou! seu palpite é maior que o número secreto.")
                        pontos -= 5
                        print(f"Pontuação: {pontos}\n")
 
                    elif palpite == numero_secreto:
                        print("Você acertou!")
                        pontos += 10
                        print(f"[ Pontuação Final: {pontos} ]")
                        break
                    else:
                        print("PALPITE INVÁLIDO! TENTE NOVAMENTE\n")
                chances_medio -= 1
                break
        elif nivel in ["difícil", "dificil", "d"]:
            while chances_dificil > 0:
                print("\n[Você tem 5 chances]")
                for i in range(chances_dificil):
                    palpite = int(input("Informe seu palpite (entre 10 e 100): "))
                    if palpite < 10 or palpite > 100:
                            print(30*"-","\nVOCÊ ERROU. Digite um número entre 10 e 100")
                            pontos -= 8
                            print(f"Pontuação: {pontos}\n")
 
                    elif palpite < numero_secreto:
                        print(30*"-","\nVocê errou! seu palpite é menor que o número secreto.")
                        pontos -= 8
                        print(f"Pontuação: {pontos}\n")
 
                    elif palpite > numero_secreto:
                        print(30*"-","\nVocê errou! seu palpite é maior que o número secreto.")
                        pontos -= 8
                        print(f"Pontuação: {pontos}\n")
 
                    elif palpite == numero_secreto:
                        print(25*"-", "\n")
                        print("Você acertou!")
                        pontos += 15
                        print(f"[ Pontuação Final: {pontos} ]")
                        break
                    else:
                        print("PALPITE INVÁLIDO! TENTE NOVAMENTE\n")
                chances_dificil -= 1
                break
        else:
            print("COMANDO INVÁLIDO. Tente novamente.")
 
        recomecar = input("Deseja tentar novamente? [sim] [não]: ").lower()
        if recomecar in ["sim", "sim", "s", "tentar", "recomecar"]:
            True
        else:
            print("\nJOGO ENCERRADO.\nFOI BOM JOGAR COM VOCÊ!\n")
            break
    except ValueError:
        print("Valor Invalido!")
        True