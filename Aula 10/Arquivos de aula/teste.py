import random

salgados = ["Coxinha", "Joelho", "Empada", "Pastel"]
salgados_certo = random.choice(salgados)
 
for i in range(1):    
    
 
    tentativas = 5
    while tentativas > 0:
 
        palpite = input("Adivinhe o salgado sorteado e receba o mesmo de graça: ")
 
        if palpite != salgados_certo:
            tentativas -= 1
            print("Este salgado não está entre os sorteados")
            print(f"Voce ainda tem {tentativas} tentativas restantes")
            #continue
        elif palpite == salgados_certo:
            print("Parabéns Você acertou e recebera o salgado de graça!")
            break        

print("O salgado sorteado foi: ", salgados_certo)