#Peça números ao usuário até que ele digite 0. Ao final, mostre a soma de todos os números digitados.

soma = 0
numero = 1

while numero != 0:
    numero = int(input("Informe um numero ou digite 0 para sair: "))
    soma = soma + numero

print(f"Soma: {soma} ")


n_tabuada=int(input('Digite um numero para ver a tabuada: '))
for i in range(1,11):
     print(n_tabuada, "x" ,i,"=",n_tabuada *i)


valor = int(input("Digite o valor: "))

for t in range(1,11):    
    print(f"{valor} x {t} = {valor * t}")