import random
numero_secreto = random.randint(10,100)
 
 
print(30*("-"))
print("Descubra O Valor da sorte")
print("------------------------------")
 
 
try:
    palpite = int(input("Digite Seu Palpite entre 10 e 100:"))
    if palpite < 10 or palpite > 100:
        print("Voce errou seu numero precisa estar entre 10 e 100!")
    else: 
        if palpite == numero_secreto:
            print("Parabéns! Voce acertou!")
        elif palpite > numero_secreto: 
            print("Voce errou, seu palpite é maior")
        else:
            print("Voce errou, seu palpite é um numero menor") 
    
   
except ValueError:
    print("valor invalido")