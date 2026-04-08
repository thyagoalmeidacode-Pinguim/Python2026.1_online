#Imports primeiro
import random

#Declarar lista
menu = ["Lasanha", "Feijoada", "Churrasco", "Pizza", "Strognof"] #Criamos a lista
prato_secreto = random.choice(menu).lower() #Seleciona um iten da lista

tentativas = 5

#Enfeite do pavão
print("== Descubra o prato secreto do Chef ==")
print(f"Você possui {tentativas} tentativas.\n")
print(20 * "-")

try:
    while tentativas > 0:
        adivinha_prato = input("Digite o nome do prato: ").lower()
        
        if adivinha_prato not in [s.lower() for s in menu]:
            print("Digite um prato válido!")
            continue

        if adivinha_prato == prato_secreto:
            print("Parabéns! Você Acertou.")
            break #Encerra o jogo
        else:
            #Diminuir a tentativa
            #tentativas = tentativas - 1
            tentativas -= 1
            print("Você errou!")
            print(f"Você ainda tem: {tentativas} tentativas ")

    #Exibe o prato escolhodo aleatorio pelo jogo         
    print(f"O prato secreto do chef é: {prato_secreto}")

except ValueError:
    print("Opçao invalida! ")