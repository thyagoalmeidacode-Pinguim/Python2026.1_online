""" 
Crie um lista vazio e peça ao usuário para inserir 4 números.
Depois, mostre:

A soma dos números
A média 

"""
#Lista vazia
notas = []

#Coletando as notas
for i in range(4):
    nt = int(input("Informe a nota: "))
    notas.append(nt)

#Exibe todas as notas
print("Notas do aluno: ", notas)
soma = sum(notas) #A função sum() soma os elemntos da lista
media = soma/len(notas)

print(f"A soma é: {soma}")
print("A média é {}".format(media))