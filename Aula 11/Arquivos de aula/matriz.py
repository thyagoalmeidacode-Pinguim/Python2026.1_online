#O que é uma matriz?
# -> Uma matriz é como uma tabela

#Criando uma matriz 3x3 (Tres linhas e duas colunas)
notas_alunos = [ 
    [8, 7, 6, 45],
    [9, 10, 5, 33],
    [2, 3, 4, 23]
]

#Analogia: Como endereço de apartamento → andar + número da porta

print("Exibir elementos da matriz")

print(notas_alunos)
print(notas_alunos[0][0]) #Exiber matriz[linha][coluna]
print(notas_alunos[1][1])

print("Tamanho da matriz")
print(f"Linhas: {len(notas_alunos)}") #Conta linhas
print(f"Colunas: {len(notas_alunos[0])}") #Conta colunas

print("Juntar as matrizes")

matriz_um = [[1,2],[3,4]]
matriz_dois = [[5,6],[7,8]]
resultado = matriz_um + matriz_dois
print(f"A soma das matrizes é: {resultado}")

print('Adcionar elementos')

numeros = [
    [2,4],
    [4,5]    
]

#numeros.append( [9,0] ) #Adiciona uma linha ao final da matriz
#print(f"Matriz com mais elementos { numeros }")

#numeros[1].append(34) #adiciona um elemento ao final de um linha da matriz
#print(f" Com numeros[0].append(10)  {numeros}")

print(f"Matriz original {numeros}")
numeros[1][0] = 78 #Substitui o elemento
print(f"A matriz numeos com novo elemento {numeros}")

numeros[0].insert(0, 67) #adiciona um valor a uma posição especifica
print(f"Com insert { numeros }")

print("Remover elementos")

nomes = [
    ["Jose", "Maria"],
    ["Marcos", "Nayara"]
]

print(f"Matriz original { nomes }")

#nomes[0].remove("Maria") #Exclui um elemnto especicifco
#print(f"Matriz removida: {nomes}")

nomes.pop(1) #remove a linha
print(f"Matriz com pop { nomes }")

print("Cotar a matriz (slice)")

matri_tres = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

print(matri_tres)

print(matri_tres[1][0:3])


print("Exibir matriz como matriz - 1")
for linha in matri_tres:
    for elemento in linha:
        print(elemento, end=" ")
    print() 


matriz = [[1,2], [3,4]]
 
for matriz in range(0, 2):
    for elemento in range(0, 2):
        print(f"[{matriz}]", end ="")
    print()