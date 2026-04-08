#Crie uma matriz 2x2 e mostre todos os elementos.
numeros = [
    [1,2,5], 
    [3,4,6]
]

#print(numeros[0][0])
#print(numeros[0][1])
#print(numeros[1][0])
#print(numeros[1][1])

for linha in numeros:
    print(f"Primeiro for le as linhas {linha}")
    for elementos in linha:
        print(f"Itens de cada coluna {elementos}")

