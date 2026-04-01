#Cria uma lista (Vetor)
#Diferente da variável que guarda um valor por vez, as listas podem guardar varios valores

frutas = [ "Maçã", "Banana", "Melancia", "Pera", "Uva" ]


#Exibir a lista
print( frutas[1] ) #Exibe um item da lista(Vetor)
print(frutas[3])  #Exibe o ultimo item da lista
print(frutas[-1]) #Exibe o ultimo item da lista
print( frutas[-2], frutas[1] )

print(20*"-")
#Tamanho da lista len()
print(len(frutas))

print(20*"-")
#Leitura da lista com for
for i in frutas:
    print(f"A fruta é {i}")

