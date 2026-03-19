# O numero secreto deverá ser aleatório
# 1 - Pesquisar sobre a função random - Servir para gerar um numero aleatório
# 2 - Permitir que o usuario escolha um numero entre 10 e 100, se ele jogar um numero menor que 10 ou maior que 100 informe que o vlaor é invalido

# Dica o random permite estabelecer um inicio e um fim
# pesquisar como limitar os valores entre 10 e 100 no random

#Importa a biblioteca do random
import random

print(30 * "-")
print("| Acerte o numero! |")
print(30 * "-")

#Definir o numero secreto(Valor aleatorio)
numero_secreto = random.randrange(10,101)
print(numero_secreto)

#Construir a lógica
#try e except servem para fazer tratamento de erros
try:
   #Solicta o palpite de quem esta jogando
    palpite = int(input("Informe seu palpite (entre 10 e 100): "))

    if palpite < 10 or palpite > 100:
        print("Valor informado esta fora do intervalo de 10 a 100.")       
    else:
        if palpite == numero_secreto:
            print("Parabéns!! Você Acertou!")
        elif palpite < numero_secreto:
            print("Você errou, seu palpite é menor que o numero secreto!")
        else:
            print("Você errou, seu palpite é maior que o numero secreto! ")

except ValueError:
    print("Valor Invalido!")