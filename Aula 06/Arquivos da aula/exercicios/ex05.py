#Peça 5 números ao usuário e mostre a soma total.

#Guarda a soma dos numeros
soma = 0 

for num in range(5):
    #Guardo o numero digitadao pelo usuario
    numero = int(input("Digite um numero: "))

    #Faço a soma dos  numero
    soma += numero
    #soma = soma + numero
print(f"A soma dos numero é: {soma}")