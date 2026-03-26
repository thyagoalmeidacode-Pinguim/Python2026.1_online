#Peça 10 números ao usuário e mostre:

#o maior número
#o menor número
numero = int(input("Informe um numero: "))

maior = numero
menor = numero

for i in range(9):
    numero = int(input("Informe um numero: "))

    if numero > maior:
        maior = numero

    if numero < menor:
        menor = numero

print("Maior", maior)
print("Mwnor", menor)