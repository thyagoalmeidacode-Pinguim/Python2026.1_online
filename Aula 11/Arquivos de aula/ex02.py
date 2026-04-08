#Crie uma matriz 2x2 e calcule a soma de todos os elementos.

#Primeira forma:
matriz = [
    [1,2],
    [3,4],
]
 
soma = matriz[0][0] + matriz[0][1] + matriz[1][0] + matriz[1][1]
print(f'O resultado da soma dos numeros da matriz é de: {soma}')

#Segunda forma
matrize = [
    [1, 2],
    [3, 4]
]
 
# somando os elementos
soma = 0
 
for linha in matrize:
    for elemento in linha:
        soma = soma+elemento
 
print("Soma:", soma)

#Terceira forma:
numeros = [
   [1,2],
   [3,4]
]

soma = sum(sum(linha) for linha in numeros)
print(soma)