#Dessa forma criamos um vetor (Lista)
lista_compras = ["Arroz", "Feijão", "Batata", "Cenoura", "Beterraba"]
                 #  0        1           2         3          4
print("Elemntos da lista")
#Exibir elementos da Lista
print(lista_compras) #Exibe a lista completa
print(lista_compras[2]) #Exibe Batata
print(lista_compras[3]) #Exibe cenoura - Ultimo item
print(lista_compras[-1]) #Exibe o ultimo item  da lista(Qunado nao sabemos o tamanho da lista)

print("Tamanho da Lista")
#Exibir o tamanho da lista
print(len(lista_compras)) #A função len() exibe o tamanho da lista

#Cortar a lista (slice)
print("Função slice (cortar)")
print(lista_compras[0:3]) #Exibe os indices 0,1,2
print(lista_compras[2:5]) 

#Concatenar Lista (Juntar as listas)
print("Juntar listas")

#Nova lista
mais_compras = ["Morango", "Uva", "Mamão"]
cesta_compras = mais_compras + lista_compras
print(cesta_compras)

#Cortar e juntar os elementos da lista
lista_um = lista_compras[2:4]
lista_dois = mais_compras[1:3]
lista_resumida = lista_um + lista_dois
print(lista_resumida)

#Verificando o maior e o menor valor de uma lista
#max() verificar dentro da lista o maior valor
#min() verificar dentro o menor valor
print("Maior e menor")
idades = [23, 43, 18, 35, 12]

print("Maior idade é: ", max(idades))
print("Menor idade é: ", min(idades))

#Adicionar elementos em uma lista
#append() - Adiciona itens ao final da nossa lista
print("Adicionando itens a nossa lista")
idades.append(78)
idades.append(21)
print(idades)

#Adcionar itens em um indice especifico da lista
#insert() - insere itens a lista em uma posição específica
print("Inserir em uma posição especifica ")
print("Idades antes da inserção:  ", idades)

idades.insert(3,"Thyago")
print("Idades apos a inserção: ", idades)

#Remover elementos da lista
#remove() remove um iten da lista

print("\nRevendo elementos da lista")
print(idades)

idades.remove(43)
print("Lista com item removido: ", idades)
idades.remove("Thyago")
print("Lista com item removido: ", idades)

#Removendo com pop()
frutas = ["Laranja", "Maçã", "Limão", "Pera"]
print(frutas)
print("Remoção com pop()")

frutas.pop(2) #Remove pelo indice
print("Iten removido com pop", frutas)

elemento = frutas.pop(2)
print("Variavel elemento: ", elemento)